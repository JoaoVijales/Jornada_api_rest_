from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Depoimentos, Destinos
from jornada.serializers import DepoimentosSerializer, DestinosSerializer
from random import choice



class DepoimentosViewSet(viewsets.ModelViewSet):
    # exibindo depoimentos #
    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializer

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    # exibindo um depoimento aleatorio #
    
    def get_id():
        queryset = Depoimentos.objects.all()
        id_list = queryset.values_list('id', flat=True)
        if id_list.count() > 0:
            id = choice(id_list)
            return id
    
    queryset = Depoimentos.objects.filter(id=get_id())
    serializer_class = DepoimentosSerializer
    
class DestinosViewSet(viewsets.ModelViewSet):
    # exibindo destinos #
    queryset = Destinos.objects.all()
    serializer_class = DestinosSerializer