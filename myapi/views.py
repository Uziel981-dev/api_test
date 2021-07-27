from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AlmacenSerializer
from .models import Almacen


class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all().order_by('name')
    serializer_class = AlmacenSerializer
