from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    picture = models.ImageField(upload_to='fotos', blank=True,)
    review = models.TextField(max_length=500, blank=False, null=False)

class Trips(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    picture = models.ImageField(upload_to='fotos', blank=True)
    price = models.CharField(max_length=50, blank=False, null=False)