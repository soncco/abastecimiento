from .models import Requerimiento
from rest_framework import serializers

class RequerimientoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Requerimiento