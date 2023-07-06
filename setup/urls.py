
from django.contrib import admin
from django.urls import path, include
from jornada.views import DepoimentosViewSet, DepoimentosHomeViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosHomeViewSet, basename='DepoimentosHome')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',    include(router.urls))
]
