var abastecimiento = abastecimiento || {};

(function() {
  abastecimiento.Detalles = Backbone.Collection.extend({
    model: abastecimiento.Detalle,
    initialize: function() {}
  });

  abastecimiento.DetallesCollection = new abastecimiento.Detalles;
})();
