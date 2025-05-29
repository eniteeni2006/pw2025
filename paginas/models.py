from django.db import models

class Resumo(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Resumo"

class Abstract(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Abstract"

class Introducao(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Introdução"

class Objetivos(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Objetivos"

class Justificativa(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Justificativa"

class RevisaoTeorica(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Revisão Teórica"

class Metodologia(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Metodologia"

class Cronograma(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Cronograma"

class Bibliografia(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Bibliografia"
