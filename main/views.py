# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from main.models import Producto
from main.forms import ProductoForm

import json

def index(request):
  return render_to_response('main/index.html', context_instance = RequestContext(request))

def test(request):
  return render_to_response('main/test.html', context_instance = RequestContext(request))

def json_productos(request):
  term = request.GET.get('term')
  productos = Producto.objects.filter(descripcion__icontains = term) | Producto.objects.filter(unidad_medida__icontains = term)
  context = []

  for producto in productos:
    context.append({
      'id': producto.pk,
      'label': '%s x %s' %(producto.unidad_medida, producto.descripcion),
      'value': '%s x %s' %(producto.unidad_medida, producto.descripcion),
    })

  return HttpResponse(json.dumps(context), mimetype = "application/json")

# Rest API
from rest_framework import viewsets, generics
from main.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

class ProductoFilterList(generics.ListAPIView):
  serializer_class = ProductoSerializer

  def get_queryset(self):
    queryset = Producto.objects.all()
    term = self.request.QUERY_PARAMS.get('term', None)

    if term is not None:
      queryset = queryset.filter(descripcion__icontains = term) | queryset.filter(unidad_medida__icontains = term)

    return queryset