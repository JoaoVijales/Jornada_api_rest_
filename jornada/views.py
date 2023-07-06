from django.shortcuts import render
from rest_framework import viewsets

class jornadaViewSet(viewsets.ModelViewSet):
    queryset = jornada.objects.all()
    serializer_class = jornadaSerializer
