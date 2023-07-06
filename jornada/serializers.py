from rest_framework import serializers
from jornada.models import Depoimentos

class DepoimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = '__all__'

    