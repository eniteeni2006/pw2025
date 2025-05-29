from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import (
    Resumo, Abstract, Introducao, Objetivos, Justificativa,
    RevisaoTeorica, Metodologia, Cronograma, Bibliografia
)

class Inicio(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'



class ResumoCreateView(CreateView):
    model = Resumo
    fields = ['conteudo']
    template_name = 'formulario.html'
    success_url = reverse_lazy('inicio')



class AbstractCreateView(CreateView):
    model = Abstract
    fields = ['conteudo']
    template_name = 'formulario.html'
    success_url = reverse_lazy('inicio')

class AbstractDetailView(DetailView):
    model = Abstract
    template_name = 'detalhe.html'

class IntroducaoCreateView(CreateView):
    model = Introducao
    fields = ['conteudo']
    template_name = 'formulario.html'
    success_url = reverse_lazy('inicio')

class IntroducaoDetailView(DetailView):
    model = Introducao
    template_name = 'detalhe.html'


