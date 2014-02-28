from django.contrib import admin
from .models import Area, Usuario, Fuente, Producto, Proyecto

admin.site.register(Area)
admin.site.register(Fuente)
admin.site.register(Producto)
admin.site.register(Proyecto)
admin.site.register(Usuario)