from django.urls import path
from .views import (
    IndexView, SobreView, CadastroUsuarioView,
    CategoriaCreate, CategoriaUpdate, CategoriaDelete,
    PostCreate, PostUpdate, PostDelete,
    AvaliacaoCreate, AvaliacaoUpdate, AvaliacaoDelete,
    ComentarioCreate, ComentarioUpdate, ComentarioDelete, 
    CategoriaList, PostList, AvaliacaoList, ComentarioList
)

# Views de autenticação do Django
from django.contrib.auth import views as auth_views

urlpatterns = [

    # URL para autenticação do usuário
    path("login/", auth_views.LoginView.as_view( 
         template_name = 'paginas/form.html',
         extra_context = {
             'titulo': 'Autenticação',
             'botao' : 'Entrar',
         }
    ),name="login"),

    #criar uma rota de logout
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),

    # Rota para alterar a senha do usuário autenticado
    path("senha/", auth_views.PasswordChangeView.as_view( 
         template_name = 'paginas/form.html',
         extra_context = {
             'titulo': 'Atualizar senha',
             'botao' : 'Salvar',
         }
    ),name="alterar-senha"),


    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('registrar/', CadastroUsuarioView.as_view(), name='registrar'),

    path('categoria/nova/', CategoriaCreate.as_view(), name='categoria_nova'),
    path('categoria/<int:pk>/editar/', CategoriaUpdate.as_view(), name='categoria_editar'),
    path('categoria/<int:pk>/excluir/', CategoriaDelete.as_view(), name='categoria_excluir'),
    path('categorias/', CategoriaList.as_view(), name='categoria_list'),

    path('post/novo/', PostCreate.as_view(), name='post_novo'),
    path('post/<int:pk>/editar/', PostUpdate.as_view(), name='post_editar'),
    path('post/<int:pk>/excluir/', PostDelete.as_view(), name='post_excluir'),
    path('posts/', PostList.as_view(), name='post_list'),

    path('avaliacao/nova/', AvaliacaoCreate.as_view(), name='avaliacao_nova'),
    path('avaliacao/<int:pk>/editar/', AvaliacaoUpdate.as_view(), name='avaliacao_editar'),
    path('avaliacao/<int:pk>/excluir/', AvaliacaoDelete.as_view(), name='avaliacao_excluir'),
    path('avaliacoes/', AvaliacaoList.as_view(), name='avaliacao_list'),

    path('comentario/novo/', ComentarioCreate.as_view(), name='comentario_novo'),
    path('comentario/<int:pk>/editar/', ComentarioUpdate.as_view(), name='comentario_editar'),
    path('comentario/<int:pk>/excluir/', ComentarioDelete.as_view(), name='comentario_excluir'),
    path('comentarios/', ComentarioList.as_view(), name='comentario_list'),
]