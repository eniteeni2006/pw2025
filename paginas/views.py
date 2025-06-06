from datetime import date
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Categoria, Comentario, Avaliação


class IndexView(TemplateView):
    model = Post
    template_name = 'paginas/index.html'
    context_object_name = 'post_list'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


#########################   CREATE   ##################################

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Nova Categoria',
        'botao': 'Criar Categoria',
    }

class PostCreate(CreateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo', 'data', 'texto', 'categoria', 'autor']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Novo Post',
        'botao': 'Publicar Post'
    }

class AvaliacaoCreate(CreateView):
    model = Avaliação
    template_name = 'paginas/form.html'
    fields = ['autor', 'nota', 'post']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Nova Avaliação',
        'botao': 'Avaliar'
    }

class ComentarioCreate(CreateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['autor', 'comentario', 'post']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Novo Comentário',
        'botao': 'Publicar Comentário'
    }


#########################   UPDATE   ##################################

class CategoriaUpdate(UpdateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Categoria',
        'botao': 'Atualizar Categoria',
    }

class PostUpdate(UpdateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo', 'data', 'texto', 'categoria', 'autor']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Post',
        'botao': 'Atualizar Post'
    }

class AvaliacaoUpdate(UpdateView):
    model = Avaliação
    template_name = 'paginas/form.html'
    fields = ['autor', 'nota', 'post']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Avaliação',
        'botao': 'Atualizar Avaliação'
    }

class ComentarioUpdate(UpdateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['autor', 'comentario', 'post']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Comentário',
        'botao': 'Atualizar Comentário'
    }

#########################   DELETE   ##################################

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Categoria',
        'botao': 'Excluir Categoria',
    }

class PostDelete(DeleteView):
    model = Post
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Post',
        'botao': 'Excluir Post',
    }

class AvaliacaoDelete(DeleteView):
    model = Avaliação
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Avaliação',
        'botao': 'Excluir Avaliação',
    }

class ComentarioDelete(DeleteView):
    model = Comentario
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Comentário',
        'botao': 'Excluir Comentário',
    }
