from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sobre/', views.sobre, name='sobre'),
    path('menu/', views.menu, name='menu'),
    path('cadastrar_aluno/', views.cadastrarAluno, name='cadastrar_aluno'),
    path('consultar_aluno/', views.consultarAluno, name='consultar_aluno'),
    path('consultar_dados/', views.consultarDados, name='consultar_dados'),
    path('cadastrar_renda/', views.cadastrarRenda, name='cadastrar_renda'),
    path('consulta_renda/', views.consultarRenda, name='consultar_renda'),
]