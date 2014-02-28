from django.conf.urls import patterns, include, url

urlpatterns = patterns('requerimiento.views',
  url(r'^requerimiento/$', 'requerimiento', name = 'requerimiento'),
  url(r'^requerimiento/nuevo$', 'requerimiento_nuevo', name = 'requerimiento_nuevo'),
)