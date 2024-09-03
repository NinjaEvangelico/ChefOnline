# publicacoes/views.py
from django.shortcuts import render, redirect
from .models import Publicacao

def lista_publicacoes(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'publicacoes/lista_publicacoes.html', {'publicacoes': publicacoes})

def criar_publicacao(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        foto = request.FILES['foto']
        Publicacao.objects.create(titulo=titulo, descricao=descricao, foto=foto, autor=request.user)
        return redirect('lista_publicacoes')
    return render(request, 'publicacoes/criar_publicacao.html')

