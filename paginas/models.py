from django.db import models
from django.contrib.auth.models import User





from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Post(models.Model):
    # permitir títulos maiores (até 255 chars) e texto sem limite mínimo/máximo
    titulo = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"


class Avaliacao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return f"Avaliação de {self.autor.username} - Nota: {self.nota} - Post: {self.post.titulo}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    # permitir comentários sem limite de comprimento
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.titulo}"