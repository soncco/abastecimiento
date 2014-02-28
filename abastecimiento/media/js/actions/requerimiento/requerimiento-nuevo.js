var abastecimiento = abastecimiento || {};

(function($) {
  $form = $('#the-form');
  $tplHidden = $('#tpl-hidden');

  getName = function(i, what) {
    return prefix + '-' + i + '-' + what;
  }

  $form.submit(function(e) {

    var i = 0;
    abastecimiento.DetallesCollection.each(function(item) {
      objProd = {
        'name': getName(i, 'cantidad'),
        'value': item.attributes.cantidad
      };
      objCant = {
        'name': getName(i, 'producto'),
        'value': item.attributes.producto
      };

      tplCantidad = Handlebars.compile($tplHidden.html());
      tplProducto = Handlebars.compile($tplHidden.html());

      htmlCantidad = tplCantidad(objCant);
      htmlProducto = tplProducto(objProd);

      $form.append(htmlCantidad);
      $form.append(htmlProducto);
      i++;
    });

    $('#id_' + prefix + '-TOTAL_FORMS').val(i);

    //$(this).submit();
  })
})(jQuery);