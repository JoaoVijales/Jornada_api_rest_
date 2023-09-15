from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Depoimentos, Trips
from jornada.serializers import ReviewsSerializer, TripsSerializer
from random import choice



class DepoimentosViewSet(viewsets.ModelViewSet):
    # exibindo depoimentos #
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    # exibindo um depoimento aleatorio #
    
    def get_id():
        queryset = Reviews.objects.all()
        id_list = queryset.values_list('id', flat=True)
        if id_list.count() > 0:
            id = choice(id_list)
            return id
    
    queryset = Reviews.objects.filter(id=get_id())
    serializer_class = ReviewsSerializer
    
class DestinosViewSet(viewsets.ModelViewSet):
    # exibindo destinos #
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer