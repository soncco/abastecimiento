from django import forms
from django.forms.models import inlineformset_factory

from models import Requerimiento, RequerimientoDetalle

class RequerimientoForm(forms.ModelForm):
  class Meta:
    model = Requerimiento

  # def __init__(self, request, *args, **kwargs):
  #   super (RequerimientoForm, self).__init__(*args, **kwargs)
  #   self.fields['creado_por'] = 1

DetalleFormSet = inlineformset_factory(Requerimiento, RequerimientoDetalle)