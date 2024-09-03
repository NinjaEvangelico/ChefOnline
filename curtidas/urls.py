# curtidas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:publicacao_id>/curtir/', views.curtir_publicacao, name='curtir_publicacao'),
]
