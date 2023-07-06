from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Depoimentos
from jornada.serializers import DepoimentosSerializer


class DepoimentosViewSet(viewsets.ModelViewSet):
    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializer

