from rest_framework import serializers
from jornada.models import Reviews, Destinos

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class DestinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = ['nome', 'foto', 'preco']
