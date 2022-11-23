from django.db import models

class Renda(models.Model):
    nome_renda = models.CharField(max_length=200)
    valor_renda = models.IntegerField()