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
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários',
                     'botao': 'Cadastrar',
                    }


    def form_valid(self, form):
        # Pegar o usuário que está autenticado
        form.instance.solicitado_por = self.request.user
        url = super().form_valid(form)

        return url

#######################

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
    # Remove do fields o campo que tem relação com User (removi o autor{autor é equivalente a user} 21/08/2025)
    fields = ['titulo',  'texto', 'categoria']
    success_url = reverse_lazy('index')
    success_message = "Post criado com sucesso!"
    extra_context = {
        'titulo': 'Novo Post',
        'botao': 'Publicar Post'
    }

    def form_valid(self, form):
        #pegar o usuario que esta autenticado
        form.instance.solicitado_por = self.request.user
        url = super().form_valid(form)
        return url

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

class SolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    model = Solicitacao
    template_name = 'paginas/form.html'
    fields = ['solicitacao']
    success_url = reverse_lazy('listar-solicitacao')
    success_message = "Solicitação bem sucedida"
    extra_context = {
        'titulo': 'Atualizar Solicitação',
        'botao': 'Salvar'
    }


    def get_objetc(self, queryset=None):
        # get_object_or_404 - busca o objeto ou retorna 404
        from django.shortcuts import get_object_or_404
        obj = get_object_or_404(Solicitacao, pk=self.kwargs['pk'], solicitado_por=self.request.user)

    return obj # type: ignore | arrumar o "Solicitacao"


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


######################  LISTAR ############################


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

class SolicitacaoList(LoginRequiredMixin, ListView):
    model = Solicitacao
    template_name = 'paginas/listas/solicitacao.html'


#Fazer uma herança para ter tudo o que tem na solicitacaoList
class MinhasSolicitacoes(SolicitacaoList):

    def get_queryset(self):
        # Como fazer consultas/filtros no django
        # Classe.objects.all() #Retorna todos os objetos
        # Classe.objects.filter(atributo=algum_valor, a2=v2)
        qs = Solicitacao.object.filter(solicitado_por=self.request.user)
        return qs
    
    def get_objetc(self, queryset=None):
        # get_object_or_404 - busca o objeto ou retorna 404
        from django.shortcuts import get_object_or_404
        obj = get_object_or_404(Solicitacao, pk=self.kwargs['pk'], solicitado_por=self.request.user)

    return obj # type: ignore | arrumar o "Solicitacao"