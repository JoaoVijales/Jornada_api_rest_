from django.db import models

class Depoimentos(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    foto = models.ImageField(upload_to='fotos', blank=True,)
    depoimento = models.TextField(max_length=500, blank=False, null=False)
