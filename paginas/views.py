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
from django.db.models import Avg
from django.contrib.auth.models import User
from .models import Post, Categoria, Comentario, Avaliacao
from .forms import UsuarioCadastroForm

class IndexView(ListView):
    model = Post
    template_name = 'paginas/index.html'
    context_object_name = 'post_list'
    # ordenar por data mais recente e buscar relações para reduzir queries
    queryset = Post.objects.select_related('autor', 'categoria').order_by('-data')

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
    def form_valid(self, form):
        # chamada durante o fluxo de POST do DeleteView (usa FormMixin)
        messages.success(self.request, "Categoria excluída com sucesso!")
        return super().form_valid(form)

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
    def form_valid(self, form):
        # usar form_valid em vez de delete para seguir a recomendação do Django
        messages.success(self.request, "Post excluído com sucesso!")
        return super().form_valid(form)
    
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
    def form_valid(self, form):
        messages.success(self.request, "Avaliação excluída com sucesso!")
        return super().form_valid(form)

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
    # ordenar lista de usuários por username
    ordering = ['username']

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

    def form_valid(self, form):
        # mensagem exibida após confirmação do formulário de deleção
        messages.success(self.request, "Usuário excluído com sucesso!")
        return super().form_valid(form)

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'paginas/listas/categoria.html'
    ordering = ['nome']

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'paginas/listas/post.html'
    paginate_by = 6
    # ordenar por data decrescente e reduzir queries com select_related
    queryset = Post.objects.select_related('autor', 'categoria').order_by('-data')


class PostDetailView(TemplateView):
    template_name = 'paginas/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        # buscar comentários e avaliações com select_related para evitar N+1
        comentarios = Comentario.objects.filter(post=post).select_related('autor').order_by('-data')
        avaliacoes = Avaliacao.objects.filter(post=post).select_related('autor')
        # calcular média das avaliações no banco de dados
        media_aggr = avaliacoes.aggregate(avg=Avg('nota'))
        media = None if media_aggr['avg'] is None else round(media_aggr['avg'], 2)
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
        texto = request.POST.get('comentario', '') or ''
        # normalizar espaços e validar
        texto = texto.strip()
        MAX_COMMENT_LENGTH = 5000
        if not texto:
            messages.error(request, 'Comentário vazio não pode ser criado.')
        elif len(texto) > MAX_COMMENT_LENGTH:
            messages.error(request, f'Comentário muito longo (máx. {MAX_COMMENT_LENGTH} caracteres).')
        else:
            Comentario.objects.create(autor=request.user, comentario=texto, post=post)
            messages.success(request, 'Comentário criado com sucesso!')
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