# publicacoes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicacoes, name='lista_publicacoes'),
    path('criar/', views.criar_publicacao, name='criar_publicacao'),
]
