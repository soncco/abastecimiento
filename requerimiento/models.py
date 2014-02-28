from django.db import models

from main.models import Usuario, Producto, Proyecto

class Requerimiento(models.Model):
  proyecto = models.ForeignKey(Proyecto)
  numero = models.CharField(max_length = 10)
  fecha = models.DateField()
  glosa = models.TextField(null = True, blank = True)
  creado_por = models.ForeignKey(Usuario)

class RequerimientoDetalle(models.Model):
  pertenece_a = models.ForeignKey(Requerimiento)
  producto = models.ForeignKey(Producto)
  cantidad = models.FloatField()
