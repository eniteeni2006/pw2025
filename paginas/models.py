from django.db import models
from django.contrib.auth.models import User





class Resumo(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Resumo"


