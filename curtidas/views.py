# curtidas/views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Curtida
from publicacoes.models import Publicacao

def curtir_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, id=publicacao_id)
    Curtida.objects.get_or_create(publicacao=publicacao, usuario=request.user)
    return redirect('lista_publicacoes')
