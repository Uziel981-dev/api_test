from rest_framework import serializers

from .models import Almacen

class AlmacenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Almacen
        fields = ('name', 'sku', 'imagen', 'tags',
        'cost', 'status', 'talla')