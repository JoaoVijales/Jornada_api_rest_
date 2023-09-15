
from django.contrib import admin
from django.urls import path, include
from jornada.views import ReviewsViewSet, ReviewsHomeViewSet, TripsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('reviews', ReviewsViewSet, basename='Reviews')
router.register('reviews-home', ReviewsHomeViewSet, basename='ReviewsHome')
router.register('trips', TripsViewSet, basename='Trips')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',    include(router.urls))
]
