from django.shortcuts import render
from rest_framework import viewsets
from jornada.models import Reviews, Trips
from jornada.serializers import ReviewsSerializer, TripsSerializer
from random import choice



class ReviewsViewSet(viewsets.ModelViewSet):
    # Displaying Reviews #
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class ReviewsHomeViewSet(viewsets.ModelViewSet):
    # Displaying a random review #
    
    def get_id():
        queryset = Reviews.objects.all()
        id_list = queryset.values_list('id', flat=True)
        if id_list.count() > 0:
            id = choice(id_list)
            return id
    
    queryset = Reviews.objects.filter(id=get_id())
    serializer_class = ReviewsSerializer
    
class TripsViewSet(viewsets.ModelViewSet):
    # Displaying trips #
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer