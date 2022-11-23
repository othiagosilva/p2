from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sobre/', views.sobre, name='sobre'),
    path('menu/', views.menu, name='menu'),
    path('financa/', views.financa, name='financa'),
]