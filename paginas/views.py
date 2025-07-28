from datetime import date
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Categoria, Comentario, Avaliação
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView







class IndexView(TemplateView):
    model = Post
    template_name = 'paginas/index.html'
    context_object_name = 'post_list'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


#########################   CREATE   ##################################

class CategoriaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    success_message = "Categoria criada com sucesso!"
    extra_context = {
        'titulo': 'Nova Categoria',
        'botao': 'Criar Categoria',
    }

class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo',  'texto', 'categoria', 'autor']
    success_url = reverse_lazy('index')
    success_message = "Post criado com sucesso!"
    extra_context = {
        'titulo': 'Novo Post',
        'botao': 'Publicar Post'
    }

class AvaliacaoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Avaliação
    template_name = 'paginas/form.html'
    fields = ['autor', 'nota', 'post']
    success_url = reverse_lazy('index')
    success_message = "Avaliação criada com sucesso!"
    extra_context = {
        'titulo': 'Nova Avaliação',
        'botao': 'Avaliar'
    }

class ComentarioCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['autor', 'comentario', 'post']
    success_url = reverse_lazy('index')
    success_message = "Comentário criado com sucesso!"
    extra_context = {
        'titulo': 'Novo Comentário',
        'botao': 'Publicar Comentário'
    }


#########################   UPDATE   ##################################

class CategoriaUpdate(LoginRequiredMixin,SuccessMessageMixin,  UpdateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    success_message = "Categoria editada com sucesso!"
    extra_context = {
        'titulo': 'Editar Categoria',
        'botao': 'Atualizar Categoria',
    }

class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo',  'texto', 'categoria', 'autor']
    success_url = reverse_lazy('index')
    success_message = "Post editado com sucesso!"
    extra_context = {
        'titulo': 'Editar Post',
        'botao': 'Atualizar Post'
    }

class AvaliacaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Avaliação
    template_name = 'paginas/form.html'
    fields = ['autor', 'nota', 'post']
    success_url = reverse_lazy('index')
    success_message = "Avaliação editada com sucesso!"
    extra_context = {
        'titulo': 'Editar Avaliação',
        'botao': 'Atualizar Avaliação'
    }

class ComentarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['autor', 'comentario', 'post']
    success_url = reverse_lazy('index')
    success_message = "Comentário editado com sucesso!"
    extra_context = {
        'titulo': 'Editar Comentário',
        'botao': 'Atualizar Comentário'
    }

#########################   DELETE   ##################################

class CategoriaDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Categoria
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    success_message = "Categoria excluida com sucesso!"
    extra_context = {
        'titulo': 'Excluir Categoria',
        'botao': 'Excluir Categoria',
    }

class PostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    success_message = "Post excluido com sucesso!"
    extra_context = {
        'titulo': 'Excluir Post',
        'botao': 'Excluir Post',
    }

class AvaliacaoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Avaliação
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    success_message = "Avaliação excluida com sucesso!"
    extra_context = {
        'titulo': 'Excluir Avaliação',
        'botao': 'Excluir Avaliação',
    }

class ComentarioDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Comentario
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    success_message = "Comentario excluido com sucesso!"
    extra_context = {
        'titulo': 'Excluir Comentário',
        'botao': 'Excluir Comentário',
    }


##################################################


class CategoriaList(LoginRequiredMixin, ListView):
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

