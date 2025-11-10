import os
import django
import sys

# Garantir que a raiz do projeto esteja no PYTHONPATH (quando o script é executado a partir de scripts/)
proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

# Ajuste do settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pw2025.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import Client
from paginas.models import Post, Categoria

username = 'testadmin'
password = 'testpass123'

# Criar ou obter superuser
user, created = User.objects.get_or_create(username=username)
if created:
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.email = 'admin@example.com'
    user.save()
    print('Superuser criado')
else:
    # garantir senha definida (para teste)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print('Superuser obtido e atualizado')

# Criar categoria mínima (se necessário)
cat, _ = Categoria.objects.get_or_create(nome='Teste')

# Criar post de teste
post = Post.objects.create(titulo='Post de teste', texto='Conteúdo', categoria=cat, autor=user)
print(f'Post criado: pk={post.pk}')

# Cliente de teste
c = Client()
login_ok = c.login(username=username, password=password)
print('Login OK?', login_ok)

# Enviar POST para excluir o post
url = f'/post/{post.pk}/excluir/'
resp = c.post(url, follow=True)
print('Status code:', resp.status_code)

# Verificar se post foi excluído
exists = Post.objects.filter(pk=post.pk).exists()
print('Post existe após tentativa de exclusão?', exists)

# Resultado final
if not exists:
    print('SUCESSO: Post excluído corretamente.')
    sys.exit(0)
else:
    print('FALHA: Post não foi excluído.')
    sys.exit(2)
