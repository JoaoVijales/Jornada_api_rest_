from rest_framework import serializers

class DepoimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = depoimentos
        fields = '__all__'

    