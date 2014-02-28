# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from main.models import Proyecto
from main.forms import ListaProyectosForm

from requerimiento.models import Requerimiento
from requerimiento.forms import RequerimientoForm, DetalleFormSet

def requerimiento(request):
  requerimientos = Requerimiento.objects.all()
  context = {'requerimientos': requerimientos}
  return render_to_response('requerimiento/lista.html', context, context_instance = RequestContext(request))

def requerimiento_nuevo(request):

  if request.method == 'POST':
    requerimiento_form = RequerimientoForm(request.POST)
    detalle_form = DetalleFormSet(request.POST)

    if requerimiento_form.is_valid() and detalle_form.is_valid():
      instance = requerimiento_form.save()
      detalle_form.instance = instance
      detalle_form.save()
      messages.success(request, 'El requerimiento ha sido creado con éxito.')

      return HttpResponseRedirect(reverse('requerimiento'))
    else:
      print "%s %s" % (requerimiento_form.errors, detalle_form.errors)
    
  proyectos = Proyecto.objects.all()
  context = {'proyectos': proyectos, 'detalle_form': DetalleFormSet}
  return render_to_response('requerimiento/nuevo.html', context, context_instance = RequestContext(request))

from rest_framework import viewsets
from requerimiento.serializers import RequerimientoSerializer

class RequerimientoViewSet(viewsets.ModelViewSet):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer