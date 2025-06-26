from datetime import date
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Categoria, Comentario, Avaliação
from django.contrib.auth.mixins import LoginRequiredMixin





class IndexView(TemplateView):
    model = Post
    template_name = 'paginas/index.html'
    context_object_name = 'post_list'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


#########################   CREATE   ##################################

class CategoriaCreate(LoginRequiredMixin, CreateView):
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
    fields = ['titulo',  'texto', 'categoria', 'autor']
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
    fields = ['titulo',  'texto', 'categoria', 'autor']
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


##################################################


class CategoriaList(ListView):
    model = Categoria
    template_name = 'paginas/listas/categoria.html'

class PostList(ListView):
    model = Post
    template_name = 'paginas/listas/post.html'

class AvaliaçãoList(ListView):
    model = Avaliação
    template_name = 'paginas/listas/avaliacao.html'

class ComentarioList(ListView):
    model = Comentario
    template_name = 'paginas/listas/comentario.html'