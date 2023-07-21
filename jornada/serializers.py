from rest_framework import serializers
from jornada.models import Depoimentos, Destinos

class DepoimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = '__all__'

class DestinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = ['nome', 'foto', 'preco']
