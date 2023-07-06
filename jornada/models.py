from django.db import models

class depoimentos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
