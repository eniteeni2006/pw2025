from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Categoria, Comentario, Avaliacao
from .forms import UsuarioCadastroForm

class IndexView(ListView):
    model = Post
    template_name = 'paginas/index.html'
    context_object_name = 'post_list'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class CadastroUsuarioView(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários', 'botao': 'Cadastrar'}

class CategoriaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    success_message = "Categoria criada com sucesso!"
    extra_context = {'titulo': 'Nova Categoria', 'botao': 'Criar Categoria'}

class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo', 'texto', 'categoria']
    success_url = reverse_lazy('index')
    success_message = "Post criado com sucesso!"
    extra_context = {'titulo': 'Novo Post', 'botao': 'Publicar Post'}
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class AvaliacaoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Avaliacao
    template_name = 'paginas/form.html'
    fields = ['nota', 'post']
    success_url = reverse_lazy('index')
    success_message = "Avaliação criada com sucesso!"
    extra_context = {'titulo': 'Nova Avaliação', 'botao': 'Avaliar'}
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ComentarioCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['comentario', 'post']
    success_url = reverse_lazy('index')
    success_message = "Comentário criado com sucesso!"
    extra_context = {'titulo': 'Novo Comentário', 'botao': 'Publicar Comentário'}
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class CategoriaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    success_message = "Categoria editada com sucesso!"
    extra_context = {'titulo': 'Editar Categoria', 'botao': 'Atualizar Categoria'}

class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['titulo', 'texto', 'categoria']
    success_url = reverse_lazy('index')
    success_message = "Post editado com sucesso!"
    extra_context = {'titulo': 'Editar Post', 'botao': 'Atualizar Post'}
    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['pk'], autor=self.request.user)

class AvaliacaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Avaliacao
    template_name = 'paginas/form.html'
    fields = ['nota', 'post']
    success_url = reverse_lazy('index')
    success_message = "Avaliação editada com sucesso!"
    extra_context = {'titulo': 'Editar Avaliação', 'botao': 'Atualizar Avaliação'}
    def get_object(self, queryset=None):
        return get_object_or_404(Avaliacao, pk=self.kwargs['pk'], autor=self.request.user)

class ComentarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['comentario', 'post']
    success_url = reverse_lazy('index')
    success_message = "Comentário editado com sucesso!"
    extra_context = {'titulo': 'Editar Comentário', 'botao': 'Atualizar Comentário'}
    def get_object(self, queryset=None):
        return get_object_or_404(Comentario, pk=self.kwargs['pk'], autor=self.request.user)

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Categoria', 'botao': 'Excluir Categoria'}
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Categoria excluída com sucesso!")
        return super().delete(request, *args, **kwargs)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Post', 'botao': 'Excluir Post'}
    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['pk'], autor=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Avaliação', 'botao': 'Excluir Avaliação'}
    def get_object(self, queryset=None):
        return get_object_or_404(Avaliacao, pk=self.kwargs['pk'], autor=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Avaliação excluída com sucesso!")
        return super().delete(request, *args, **kwargs)

class ComentarioDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Comentário', 'botao': 'Excluir Comentário'}
    def get_object(self, queryset=None):
        return get_object_or_404(Comentario, pk=self.kwargs['pk'], autor=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Comentário excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'paginas/listas/categoria.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'paginas/listas/post.html'

class AvaliacaoList(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'paginas/listas/avaliacao.html'

class ComentarioList(LoginRequiredMixin, ListView):
    model = Comentario
    template_name = 'paginas/listas/comentario.html'