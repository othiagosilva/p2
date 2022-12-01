from django.db import models

class Usuario(models.Model):
    email = models.EmailField(null = True)
    usuario = models.CharField(max_length=20, null = True)
    senha = models.CharField(max_length=200, null = True)
    treinador = models.BooleanField(null = True)

class Renda(models.Model):
    nome_renda = models.CharField(max_length=20, null = True)
    valor_renda = models.IntegerField(null = True)

class Aluno(models.Model):
    nome = models.CharField(max_length=20, null = True)
    idade = models.CharField(max_length=20, null = True)
    peso = models.CharField(max_length=20, null = True)
    altura = models.CharField(max_length=20, null = True)
    masculino = models.BooleanField(default=True, null = True)
    cintura = models.CharField(max_length=20, null = True)
    quadril = models.CharField(max_length=20, null = True)
    subescapular = models.CharField(max_length=20, null = True)
    tricipital = models.CharField(max_length=20, null = True)
    peitoral = models.CharField(max_length=20, null = True)
    axilar_medio = models.CharField(max_length=20, null = True)
    suprailiaca = models.CharField(max_length=20, null = True)
    coxa = models.CharField(max_length=20, null = True)
    abdomen_dobra = models.CharField(max_length=20, null = True)
    torax = models.CharField(max_length=20, null = True)
    braco_relaxado = models.CharField(max_length=20, null = True)
    braco_contraido = models.CharField(max_length=20, null = True)
    antebraco = models.CharField(max_length=20, null = True)
    abdomen_perimetria = models.CharField(max_length=20, null = True)
    cintura = models.CharField(max_length=20, null = True)
    quadril = models.CharField(max_length=20, null = True)
    coxas = models.CharField(max_length=20, null = True)
    panturrilha = models.CharField(max_length=20, null = True)