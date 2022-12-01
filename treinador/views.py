from django.shortcuts import HttpResponse, render
from .models import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import  Response
from treinador.serializers import RendaSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from .models import Aluno, Renda
import psycopg2 as pg

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sobre(request):
    return render(request, 'sobre.html')
    
def menu(request):
    return render(request, 'menu.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(email=email, password=senha) # faz a autenticação

        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')

def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma')
    return HttpResponse('Você precisa estar logado')

def cadastrarAluno(request):
    alunos = Aluno.objects

    if request.method == "GET":
        return render(request, 'cadastrar_aluno.html')
    else:
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')

        # user = User.objects.filter(username=nome).first # trás todos os usuários que tiverem o mesmo nome

        # if user:
        #     return HttpResponse('Já existe um usuário com esse nome')
        
        alunos.nome = nome
        alunos.idade = idade
        alunos.peso = peso
        alunos.altura = altura
        # user = User.objects.create_user(nome, idade, peso, altura)
        alunos.save()

        return HttpResponse('Usuário cadastrado com sucesso')

def consultarAluno(request):
    alunos = Aluno.objects.all()

    return render(request, "consultar_aluno.html", {"alunos":alunos}) # para conseguir acessar lá no html

def alterarAluno(request):
    alunos = Aluno.objects

    if request.method == "GET":
        return render(request, 'alterar_aluno.html')
    else:
        if alunos.id == Aluno.objects.get('id'):

            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            peso = request.POST.get('peso')
            altura = request.POST.get('altura')

            alunos.nome = nome
            alunos.idade = idade
            alunos.peso = peso
            alunos.altura = altura
            alunos.save()

            return HttpResponse('Usuário alterado com sucesso')

def consultarDados(request):

    return render(request, 'consultar_dados.html')

def alterarRenda(request):
    renda = Renda.objects

    if request.method == "GET":
        return render(request, 'alterar_aluno.html')
    else:
        if renda.id == Renda.objects.get('id'):

            nome = request.POST.get('nome')
            valor = request.POST.get('valor')

            renda.nome_renda = nome
            renda.valor_renda = valor
            renda.save()

            return HttpResponse('Usuário alterado com sucesso')
    return render(request, 'alterar_renda.html')

@api_view(['GET', 'POST'])
def cadastrarRenda(request):

    if request.method == "GET":
        return render(request, 'cadastrar_renda.html')
    else:
        nome_renda = request.POST.get('nome_renda')
        valor_renda = request.POST.get('valor_renda')
        
        rendas = Renda.objects.get_or_create(nome_renda=nome_renda, valor_renda=valor_renda)
        return Response(rendas, 200)

def consultarRenda(request):
    rendas = Renda.objects.all()

    return render(request, "consultar_renda.html", {"rendas":rendas})

@api_view(['GET', 'POST', 'DELETE'])
def renda_list(request):
    # Retorna, cadastra e deleta as rendas
    if request.method == 'GET':
        rendas = Renda.objects.all()
            
        title = request.GET.get('title', None)
        if title is not None:
            rendas = rendas.filter(title__icontains=title)
        
        rendas_serializer = RendaSerializer(rendas, many=True)
        return JsonResponse(rendas_serializer.data, safe=False)

    elif request.method == 'POST':
        renda_data = JSONParser().parse(request)
        rendas_serializer = RendaSerializer(data=renda_data)
        if rendas_serializer.is_valid():
            rendas_serializer.save()
            return JsonResponse(rendas_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(rendas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Renda.objects.all().delete()
        return JsonResponse({'message': '{} rendas deletadas.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def renda_detail(request, pk):
    # Retorna a reda pelo código informado
    try: 
        renda = Renda.objects.get(pk=pk) 

        if request.method == 'GET': 
            rendas_serializer = RendaSerializer(renda) 
            return JsonResponse(rendas_serializer.data)  

        elif request.method == 'PUT': 
            renda_data = JSONParser().parse(request) 
            rendas_serializer = RendaSerializer(renda, data=renda_data) 
            if rendas_serializer.is_valid(): 
                rendas_serializer.save() 
                return JsonResponse(rendas_serializer.data) 
            return JsonResponse(rendas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            renda.delete() 
            return JsonResponse({'message': 'Renda deletada.'}, status=status.HTTP_204_NO_CONTENT)
    except Renda.DoesNotExist: 
        return JsonResponse({'message': 'Ops! A renda não existe'}, status=status.HTTP_404_NOT_FOUND)
 
@api_view(['GET'])
def tutorial_list_published(request):
    # Retorna todas as rendas cadastradas
    rendas = Renda.objects.filter(published=True)
        
    if request.method == 'GET': 
        rendas_serializer = RendaSerializer(rendas, many=True)
        return JsonResponse(rendas_serializer.data, safe=False)  