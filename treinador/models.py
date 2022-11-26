from django.db import models

class Usuario(models.Model):
    codigo = models.IntegerField(primary_key=True,default = 0)
    email = models.EmailField()
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=200)
    treinador = models.BooleanField()

class Renda(models.Model):
    codigo = models.IntegerField(primary_key=True, default = 0)
    nome_renda = models.CharField(max_length=20)
    valor_renda = models.IntegerField()

class Aluno(models.Model):
    codigo = models.IntegerField(primary_key=True, default=0)
    nome = models.CharField(max_length=20)
    idade = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    altura = models.CharField(max_length=20)
    masculino = models.BooleanField(default=True)
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