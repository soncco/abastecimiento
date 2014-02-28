from django import forms

from models import Proyecto, Producto

class ListaProyectosForm(forms.Form):
  proyectos = forms.ModelChoiceField(queryset = Proyecto.objects.all())

class ProductoForm(forms.ModelForm):
  class Meta:
    model = Producto