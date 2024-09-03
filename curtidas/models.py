# curtidas/models.py
from django.contrib.auth.models import User
from django.db import models
from publicacoes.models import Publicacao

class Curtida(models.Model):
    publicacao = models.ForeignKey(Publicacao, related_name='curtidas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('publicacao', 'usuario')

    def __str__(self):
        return f'Curtida de {self.usuario} em {self.publicacao}'
