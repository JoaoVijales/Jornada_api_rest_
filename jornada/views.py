from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Depoimentos
from jornada.serializers import DepoimentosSerializer
from random import randint


class DepoimentosViewSet(viewsets.ModelViewSet):
    # exibindo depoimentos #
    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializer

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    # exibindo um depoimento aleatorio #
    if Depoimentos.objects.count() > 0:
        total_objects = Depoimentos.objects.count() -1
        id = randint(0, total_objects)
        queryset = Depoimentos.objects.filter(id=id)
        serializer_class = DepoimentosSerializer