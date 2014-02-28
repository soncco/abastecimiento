from django.conf.urls import patterns, include, url

from rest_framework import routers
from main.views import ProductoViewSet, ProductoFilterList

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = patterns('main.views',
  url(r'^$', 'index', name = 'index'),
  url(r'^test$', 'test', name = 'test'),

  # API
  url(r'^api/', include(router.urls)),
  url(r'^api/productos-filter/$', ProductoFilterList.as_view()),
)