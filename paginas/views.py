from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
        # permite que o autor do post ou um superuser edite o post
        if self.request.user.is_superuser:
            return get_object_or_404(Post, pk=self.kwargs['pk'])
        return get_object_or_404(Post, pk=self.kwargs['pk'], autor=self.request.user)

class AvaliacaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Avaliacao
    template_name = 'paginas/form.html'
    fields = ['nota', 'post']
    success_url = reverse_lazy('index')
    success_message = "Avaliação editada com sucesso!"
    extra_context = {'titulo': 'Editar Avaliação', 'botao': 'Atualizar Avaliação'}
    def get_object(self, queryset=None):
        if self.request.user.is_superuser:
            return get_object_or_404(Avaliacao, pk=self.kwargs['pk'])
        return get_object_or_404(Avaliacao, pk=self.kwargs['pk'], autor=self.request.user)

class ComentarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comentario
    template_name = 'paginas/form.html'
    fields = ['comentario', 'post']
    success_url = reverse_lazy('index')
    success_message = "Comentário editado com sucesso!"
    extra_context = {'titulo': 'Editar Comentário', 'botao': 'Atualizar Comentário'}
    def get_object(self, queryset=None):
        if self.request.user.is_superuser:
            return get_object_or_404(Comentario, pk=self.kwargs['pk'])
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
        # permite que o autor do post ou um superuser exclua o post
        if self.request.user.is_superuser:
            return get_object_or_404(Post, pk=self.kwargs['pk'])
        return get_object_or_404(Post, pk=self.kwargs['pk'], autor=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        # bloquear acesso à página de confirmação para usuários não autorizados
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if not (request.user.is_superuser or post.autor == request.user):
            messages.error(request, "Você não tem permissão para excluir este post.")
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # bloquear tentativa de exclusão via POST para usuários não autorizados
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if not (request.user.is_superuser or post.autor == request.user):
            messages.error(request, "Você não tem permissão para excluir este post.")
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Avaliação', 'botao': 'Excluir Avaliação'}
    def get_object(self, queryset=None):
        if self.request.user.is_superuser:
            return get_object_or_404(Avaliacao, pk=self.kwargs['pk'])
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
        if self.request.user.is_superuser:
            return get_object_or_404(Comentario, pk=self.kwargs['pk'])
        return get_object_or_404(Comentario, pk=self.kwargs['pk'], autor=self.request.user)

class UsuarioList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'paginas/listas/usuario.html'
    context_object_name = 'user_list'

    def test_func(self):
        return self.request.user.is_superuser


class UsuarioUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('usuarios')
    success_message = "Usuário editado com sucesso!"
    extra_context = {'titulo': 'Editar Usuário', 'botao': 'Atualizar Usuário'}

    def test_func(self):
        return self.request.user.is_superuser


class UsuarioDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('usuarios')
    extra_context = {'titulo': 'Excluir Usuário', 'botao': 'Excluir Usuário'}

    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        # Interceptar POST para evitar que um usuário exclua a si mesmo
        obj = self.get_object()
        if obj.pk == request.user.pk:
            messages.error(request, "Você não pode excluir o seu próprio usuário.")
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Usuário excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'paginas/listas/categoria.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'paginas/listas/post.html'
    paginate_by = 6


class PostDetailView(TemplateView):
    template_name = 'paginas/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        comentarios = Comentario.objects.filter(post=post).order_by('-data')
        avaliacoes = Avaliacao.objects.filter(post=post)
        # calcular média das avaliações, se existirem
        media = None
        if avaliacoes.exists():
            media = round(sum(a.nota for a in avaliacoes) / avaliacoes.count(), 2)
        context.update({
            'object': post,
            'comentarios': comentarios,
            'avaliacoes': avaliacoes,
            'media_avaliacao': media,
        })
        return context


@login_required
def comentar_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        texto = request.POST.get('comentario')
        if texto:
            Comentario.objects.create(autor=request.user, comentario=texto, post=post)
            messages.success(request, 'Comentário criado com sucesso!')
        else:
            messages.error(request, 'Comentário vazio não pode ser criado.')
    return redirect('post_detail', pk=pk)


@login_required
def avaliar_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        try:
            nota = int(request.POST.get('nota'))
        except (TypeError, ValueError):
            messages.error(request, 'Nota inválida.')
            return redirect('post_detail', pk=pk)
        # impedir múltiplas avaliações do mesmo usuário no mesmo post: atualizar se já existir
        aval, created = Avaliacao.objects.update_or_create(
            autor=request.user,
            post=post,
            defaults={'nota': nota}
        )
        if created:
            messages.success(request, 'Avaliação criada com sucesso!')
        else:
            messages.success(request, 'Avaliação atualizada com sucesso!')
    return redirect('post_detail', pk=pk)

class AvaliacaoList(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'paginas/listas/avaliacao.html'

class ComentarioList(LoginRequiredMixin, ListView):
    model = Comentario
    template_name = 'paginas/listas/comentario.html'
    paginate_by = 10