from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.urls import reverse_lazy
from .models import (Post, Categoria, Comentario, Avaliação, User)

class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'



class PostCreate(CreateView):
    model = Post
    template_name = 'paginas/form.html'
    fields = ['título, data, texto']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Post',
        'data': date.today().strftime('%d/%m/%Y'),
        'texto' : 'Digite Aqui...',
        'botao': 'Enviar Post' 
    }

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'paginas/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')



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


###########################################################


