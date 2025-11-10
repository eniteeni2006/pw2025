from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Categoria, Avaliacao
from django.urls import reverse


class DeleteTests(TestCase):
	def setUp(self):
		# Criar superuser de teste
		self.admin = User.objects.create_superuser(username='tadmin', email='a@a.com', password='pass1234')
		# Criar categoria e post
		self.cat = Categoria.objects.create(nome='CatTeste')
		self.post = Post.objects.create(titulo='T1', texto='Texto', categoria=self.cat, autor=self.admin)
		self.client = Client()
		self.client.login(username='tadmin', password='pass1234')

	def test_admin_can_delete_post(self):
		url = reverse('post_excluir', args=[self.post.pk])
		resp = self.client.post(url, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

	def test_admin_cannot_delete_self(self):
		# tentar excluir o próprio usuário
		url = reverse('usuario_excluir', args=[self.admin.pk])
		resp = self.client.post(url, follow=True)
		# usuário deve continuar existindo
		self.assertTrue(User.objects.filter(pk=self.admin.pk).exists())
		# verificar que mensagem de erro foi adicionada (status 200 e redirect)
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Você não pode excluir o seu próprio usuário.')

	def test_other_user_cannot_delete_post(self):
		# criar outro usuário e tentar excluir o post do admin
		other = User.objects.create_user(username='outro', password='pass2')
		self.client.logout()
		self.client.login(username='outro', password='pass2')
		url = reverse('post_excluir', args=[self.post.pk])
		resp = self.client.post(url, follow=True)
		# post deve continuar existindo
		self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())
		# deve haver mensagem de permissão negada
		self.assertContains(resp, 'Você não tem permissão para excluir este post.')


class TemplateButtonTests(TestCase):
	def setUp(self):
		# usuários e post de exemplo
		self.author = User.objects.create_user(username='autor', password='a123')
		self.other = User.objects.create_user(username='outro', password='b123')
		self.admin = User.objects.create_superuser(username='super', email='s@x.com', password='s123')
		self.cat = Categoria.objects.create(nome='CatX')
		self.post = Post.objects.create(titulo='Titulo', texto='Texto', categoria=self.cat, autor=self.author)
		self.client = Client()

	def test_author_sees_edit_delete_buttons_in_list_and_detail(self):
		self.client.login(username='autor', password='a123')
		list_url = reverse('post_list')
		detail_url = reverse('post_detail', args=[self.post.pk])
		edit_url = reverse('post_editar', args=[self.post.pk])
		delete_url = reverse('post_excluir', args=[self.post.pk])

		resp_list = self.client.get(list_url)
		self.assertEqual(resp_list.status_code, 200)
		self.assertContains(resp_list, edit_url)
		self.assertContains(resp_list, delete_url)

		resp_detail = self.client.get(detail_url)
		self.assertEqual(resp_detail.status_code, 200)
		self.assertContains(resp_detail, edit_url)
		self.assertContains(resp_detail, delete_url)


class AvaliacaoUpsertTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='u1', password='p1')
		self.cat = Categoria.objects.create(nome='C1')
		self.post = Post.objects.create(titulo='P1', texto='T', categoria=self.cat, autor=self.user)
		self.client = Client()
		self.client.login(username='u1', password='p1')

	def test_upsert_avaliacao(self):
		url = reverse('post_avaliar', args=[self.post.pk])
		# primeira avaliação
		resp = self.client.post(url, {'nota': '4'}, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(Avaliacao.objects.filter(post=self.post, autor=self.user).count(), 1)
		self.assertEqual(Avaliacao.objects.get(post=self.post, autor=self.user).nota, 4)
		# atualizar avaliação
		resp2 = self.client.post(url, {'nota': '2'}, follow=True)
		self.assertEqual(resp2.status_code, 200)
		self.assertEqual(Avaliacao.objects.filter(post=self.post, autor=self.user).count(), 1)
		self.assertEqual(Avaliacao.objects.get(post=self.post, autor=self.user).nota, 2)
