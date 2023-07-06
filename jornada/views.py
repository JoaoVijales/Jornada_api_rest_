from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Depoimentos
from jornada.serializers import DepoimentosSerializer
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
        id = choice(id_list)
        return id
    
    queryset = Depoimentos.objects.filter(id=get_id())
    serializer_class = DepoimentosSerializer
    