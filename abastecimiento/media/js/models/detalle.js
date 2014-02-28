var abastecimiento = abastecimiento || {};

(function() {

  abastecimiento.Detalle = Backbone.Model.extend({
    defaults: function() {
      return {
        cantidad: 1,
        producto: 0,
      }
    },

    validate: function(attribs) {
      if(attribs.producto < 0) {
        return 'No haz escogido un producto';
      }

      if(attribs.cantidad < 1) {
        return 'La cantidad debe ser mayor que cero';
      }
    },

    initialize: function() {
      this.on('invalid', function(model, error){
        alert(error);
      });
    }
  });
})();
