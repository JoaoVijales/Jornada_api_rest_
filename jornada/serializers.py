from rest_framework import serializers
from jornada.models import Reviews, Trips

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ['name', 'picture', 'price']
