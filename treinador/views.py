from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sobre(request):
    return render(request, 'sobre.html')
    
def menu(request):
    return render(request, 'menu.html')

def cadastrarRenda(request):
    return render(request, 'cadastrar_renda.html')

def consultarRenda(request):
    return render(request, 'consulta_renda.html')