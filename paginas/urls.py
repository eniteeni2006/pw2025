from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CadastroUsuarioView
from .views import MinhasSolicitacoes


from .views import (
    IndexView, SobreView,
    CategoriaCreate, CategoriaUpdate, CategoriaDelete,
    PostCreate, PostUpdate, PostDelete,
    AvaliacaoCreate, AvaliacaoUpdate, AvaliacaoDelete,
    ComentarioCreate, ComentarioUpdate, ComentarioDelete, 
    CategoriaList, PostList, AvaliaçãoList,
    ComentarioList

    )

urlpatterns = [
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

    #Criar rota para pgn de login
    path("login/", auth_views.LoginView.as_view(
        template_name = 'paginas/form.html',
        extra_context = {
        'titulo': 'Autenticação',
        'botao': 'Entrar',}
    ), name="login"),

     path("senha/", auth_views.PasswordChangeView.as_view(
        template_name = 'paginas/form.html',
        extra_context = {
        'titulo': 'Atualizar senha',
        'botao': 'Salvar',}
    ), name="senha"),

    #Criar uma rota de logout
    path("Sair/", auth_views.LogoutView.as_view(), name="Sair"),

    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),

    # Categoria
    path('categoria/nova/', CategoriaCreate.as_view(), name='categoria_nova'),
    path('categoria/<int:pk>/editar/', CategoriaUpdate.as_view(), name='categoria_editar'),
    path('categoria/<int:pk>/excluir/', CategoriaDelete.as_view(), name='categoria_excluir'),
    path('categoria/listar/', CategoriaList.as_view(), name='categoria_listar'),

    # Post
    path('post/novo/', PostCreate.as_view(), name='post_novo'),
    path('post/<int:pk>/editar/', PostUpdate.as_view(), name='post_editar'),
    path('post/<int:pk>/excluir/', PostDelete.as_view(), name='post_excluir'),
    path('post/listar/', PostList.as_view(), name='post_listar'),

    # Avaliação
    path('avaliacao/nova/', AvaliacaoCreate.as_view(), name='avaliacao_nova'),
    path('avaliacao/<int:pk>/editar/', AvaliacaoUpdate.as_view(), name='avaliacao_editar'),
    path('avaliacao/<int:pk>/excluir/', AvaliacaoDelete.as_view(), name='avaliacao_excluir'),
    path('avaliacao/listar/', AvaliaçãoList.as_view(), name='avaliacao_listar'),


    # Comentário
    path('comentario/novo/', ComentarioCreate.as_view(), name='comentario_novo'),
    path('comentario/<int:pk>/editar/', ComentarioUpdate.as_view(), name='comentario_editar'),
    path('comentario/<int:pk>/excluir/', ComentarioDelete.as_view(), name='comentario_excluir'),
    path('comentario/listar/', ComentarioList.as_view(), name='comentario_listar'),

    # URL PRA "MinhasSolicitacoes" path("listar/minhas-solicitacoes/"), MinhasSolicitacoes.as_view, name = '' (perdi o fio da miada)
]
