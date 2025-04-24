from django.db import models

# todas as classes deve ter herança de models.Model
# Create your models here.
# Para fazer uma herança em py basta colocar o nome da classe entre parenteses




# Cadastrar alunos (nome, CPF, curso)

#Cadastrar cursos (nome, código, duração)

#Listar alunos por curso

#Salvar os dados em um arquivo .json

#Carregar os dados ao iniciar o programa








# Cria sua classes
class Campus(models.Model):
    #Definir atributos
    nome = models.CharField(max_length = 100) # Charfield (campo de texto comum) || Textfield (campo de texto grande) || Datefield (campo para data)

class Curso(models.Model):
    nome = models.CharField(max_length = 150)
    duracao = models.CharField(max_length = 50, verbose_name = "duração")
    campus = models.ForeignKey(Campus, on_delete = models.PROTECT)

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    curso = models.CharField(max_length=50)

class SistemaDeCadastro(models.Model):
    alunos = models.CharField(max_length=50)
    cursos = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)

class CadastrarAluno(models.Model):
    nome = input("Digite o nome do aluno:")
    cpf = input("CPF Do aluno:")

