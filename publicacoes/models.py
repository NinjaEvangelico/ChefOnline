from django.contrib.auth.models import User
from django.db import models

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='fotos_receitas/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

