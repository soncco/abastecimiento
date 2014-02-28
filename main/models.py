from django.db import models
from django.contrib.auth.models import User
from decimal import *

class Producto(models.Model):
  unidad_medida = models.CharField(max_length = 10)
  descripcion = models.TextField()

  def __unicode__(self):
    return self.descripcion

class Fuente(models.Model):
  nombre = models.CharField(max_length = 100)

  def __unicode__(self):
    return self.nombre

class Proyecto(models.Model):
  fuente = models.ManyToManyField(Fuente)
  anio = models.IntegerField()
  nombre = models.CharField(max_length = 255, default = '')

  def __unicode__(self):
    return self.nombre

class Area(models.Model):
  nombre = models.CharField(max_length = 100)

  def __unicode__(self):
    return self.nombre

class Usuario(models.Model):
  usuario = models.OneToOneField(User)
  area = models.ManyToManyField(Area)
  proyecto = models.ManyToManyField(Proyecto)

  def __unicode__(self):
    return self.usuario.username