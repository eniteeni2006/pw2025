from django.db import models
from django.contrib.auth.models import User





from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"


class Avaliação(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return f"Avaliação de {self.autor.username} - Nota: {self.nota} - Post: {self.post.titulo}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.titulo}"