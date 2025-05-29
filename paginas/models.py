from django.db import models
from django.contrib.auth.models import User





class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

class Avaliação(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)