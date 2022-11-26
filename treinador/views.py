from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sobre(request):
    return render(request, 'sobre.html')
    
def menu(request):
    return render(request, 'menu.html')

def cadastrarAluno(request):
    return render(request, 'cadastrar_aluno.html')

def consultarAluno(request):
    alunos = Aluno.objects.all()

    dados = {
        'alunos' : alunos
    }

    return render(request, 'consultar_aluno.html', dados)

def consultarDados(request):
    return render(request, 'consultar_dados.html')

def cadastrarRenda(request):
    return render(request, 'cadastrar_renda.html')

def consultarRenda(request):
    rendas = Renda.objects.all()

    dados = {
     'rendas' : rendas
    }

    return render(request, 'consulta_renda.html', dados)