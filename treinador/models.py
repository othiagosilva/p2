from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=200)
    tipo_usuario = models.BooleanField()

class Renda(models.Model):
    nome_renda = models.CharField(max_length=20)
    valor_renda = models.IntegerField()

class Aluno(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    altura = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    cintura = models.CharField(max_length=20)
    quadril = models.CharField(max_length=20)
    subescapular = models.CharField(max_length=20)
    tricipital = models.CharField(max_length=20)
    peitoral = models.CharField(max_length=20)
    axilar_medio = models.CharField(max_length=20)
    suprailiaca = models.CharField(max_length=20)
    coxa = models.CharField(max_length=20)
    abdomen_dobra = models.CharField(max_length=20)
    torax = models.CharField(max_length=20)
    braco_relaxado = models.CharField(max_length=20)
    braco_contraido = models.CharField(max_length=20)
    antebraco = models.CharField(max_length=20)
    abdomen_perimetria = models.CharField(max_length=20)
    cintura = models.CharField(max_length=20)
    quadril = models.CharField(max_length=20)
    coxas = models.CharField(max_length=20)
    panturrilha = models.CharField(max_length=20)