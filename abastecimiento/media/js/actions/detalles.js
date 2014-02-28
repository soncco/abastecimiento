var abastecimiento = abastecimiento || {};

(function($) {
  $detalles = $('#detalles');
  $tplDetalle = $('#tpl-detalle-row');
  $tplNone = $('#tpl-detalle-none')

  removeDetalle = function(e) {
    if($detalles.find('tr').length > 1)
      $(e.delegateTarget).parent().parent().remove();
    else {
      $(e.delegateTarget)
        .data('content', 'Debe haber al menos un detalle.');
      $(e.delegateTarget).popover();
      $(e.delegateTarget).popover('toggle');
    }
  }

  var autoCompleteOptions = {
    minLength: 1,
    source: function(request, response) {
      $.ajax({
        url: '/api/productos-filter/',
        dataType: 'json',
        data: {
          term: request.term
        },
        success: function(data, e, xhr) {
          if(e)
          response($.map(data, function (item) {
            return {
              data: item,
              label: item.unidad_medida + ' x ' + item.descripcion,
              value: item.unidad_medida + ' x ' + item.descripcion,
            }
          }));
        }
      })
    },
    response: function(e, ui) {
      if(ui.content.length === 0) {
        var parent = $(e.target).parent();
        parent.find('.message-no-existe').remove();
        parent.append($tplNone.html());
        parent.find('.message-no-existe a').click(function() {
          parent.find('.autocomplete-productos').val('');
        });
      }
    },
    select: function(e, ui) {
      var parent = $(e.target).parent();
      parent.find('.message-no-existe').remove();
      abastecimiento.DetallesCollection.add({
        'cantidad': parent.parent().find('.cantidad').val(),
        'producto': ui.item.id
      }, {'validate': true});
    },
  }

  $('#add-detalle').click(function() {

    $detalles.find('.remove-detalle').popover('destroy');

    row = $($tplDetalle.html());
    $detalles.append(row);
    row.find('.remove-detalle').click(removeDetalle);
    row.find('.autocomplete-productos').autocomplete(autoCompleteOptions);
  });

  $('.remove-detalle').click(removeDetalle);

  $('.autocomplete-productos').autocomplete(autoCompleteOptions);

  $('#modal-product').on('show.bs.modal', function (e) {
    $('.message-no-existe').remove();

    $('#unidad_medida').val('');
    $('#descripcion').val('');
  });

  $('#form-product').submit(function(e) {
    e.preventDefault();
    $.post('/api/productos/', $(this).serialize())
      .done(function(data, status, xhr) {
        if(status == 'success')
          $('#modal-product').modal('hide');
      });
  });

})(jQuery)
