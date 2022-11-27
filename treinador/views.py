from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from treinador.serializers import RendaSerializer
from rest_framework.decorators import api_view

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