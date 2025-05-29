from django.urls import path
from .views import (
    Inicio, SobreView,
    ResumoCreateView, ResumoDetailView,
    AbstractCreateView, AbstractDetailView,
    IntroducaoCreateView, IntroducaoDetailView
)

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),

    path('resumo/novo/', ResumoCreateView.as_view(), name='resumo_novo'),
    path('resumo/<int:pk>/', ResumoDetailView.as_view(), name='resumo_detalhe'),

    path('abstract/novo/', AbstractCreateView.as_view(), name='abstract_novo'),
    path('abstract/<int:pk>/', AbstractDetailView.as_view(), name='abstract_detalhe'),

    path('introducao/novo/', IntroducaoCreateView.as_view(), name='introducao_novo'),
    path('introducao/<int:pk>/', IntroducaoDetailView.as_view(), name='introducao_detalhe'),

]
