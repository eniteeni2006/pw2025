from django.urls import path
from .views import (
    IndexView, SobreView,
    CategoriaCreate, CategoriaUpdate, CategoriaDelete,
    PostCreate, PostUpdate, PostDelete,
    AvaliacaoCreate, AvaliacaoUpdate, AvaliacaoDelete,
    ComentarioCreate, ComentarioUpdate, ComentarioDelete
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),

    # Categoria
    path('categoria/nova/', CategoriaCreate.as_view(), name='categoria_nova'),
    path('categoria/<int:pk>/editar/', CategoriaUpdate.as_view(), name='categoria_editar'),
    path('categoria/<int:pk>/excluir/', CategoriaDelete.as_view(), name='categoria_excluir'),

    # Post
    path('post/novo/', PostCreate.as_view(), name='post_novo'),
    path('post/<int:pk>/editar/', PostUpdate.as_view(), name='post_editar'),
    path('post/<int:pk>/excluir/', PostDelete.as_view(), name='post_excluir'),

    # Avaliação
    path('avaliacao/nova/', AvaliacaoCreate.as_view(), name='avaliacao_nova'),
    path('avaliacao/<int:pk>/editar/', AvaliacaoUpdate.as_view(), name='avaliacao_editar'),
    path('avaliacao/<int:pk>/excluir/', AvaliacaoDelete.as_view(), name='avaliacao_excluir'),

    # Comentário
    path('comentario/novo/', ComentarioCreate.as_view(), name='comentario_novo'),
    path('comentario/<int:pk>/editar/', ComentarioUpdate.as_view(), name='comentario_editar'),
    path('comentario/<int:pk>/excluir/', ComentarioDelete.as_view(), name='comentario_excluir'),
]
