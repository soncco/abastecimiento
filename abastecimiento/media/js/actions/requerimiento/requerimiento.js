var abastecimiento = abastecimiento || {};

(function($) {
  $view = $('.view');
  $modalQuick = $('#modal-quick');

  $view.click(function() {
    rid = $(this).data('rid');
    
    $modalQuick.modal();
  });
})(jQuery);