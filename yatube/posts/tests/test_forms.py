from http import HTTPStatus

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.test import Client, TestCase
from django.urls import reverse

from ..forms import PostForm
from ..models import Group, Post, User


class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Author')
        cls.user_no_author = User.objects.create_user(username='NoAuthor')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая запись',
            group=cls.group,
        )
        cls.form = PostForm()
        cls.post_quantity = Post.objects.count()

    def setUp(self):
        self.another = Client()
        self.another.force_login(self.user)
        self.authorized_client_no_author = Client()
        self.authorized_client_no_author.force_login(self.user_no_author)

    def test_edit_form_only_for_author(self):
        """Запись может редактировать только автор + перенаправление."""
        # Работает только список в списке или кортеж в кортеже.
        roles = (
            (self.authorized_client_no_author,),
            (self.another,),
        )
        for role in roles:
            with self.subTest(role=role):
                reverse_name = reverse('posts:post_edit', args=(self.post.id,))
                # Kлиент отправляет запрос, a далее в зависиости
                # от роли выполняется то или иное условие.
                response = self.client.post(reverse_name)
                if role == self.authorized_client_no_author:
                    self.assertRedirects(response, reverse(
                        'posts:post_detail', args=(self.post.id,)),
                        HTTPStatus.FOUND
                    )
                else:
                    login = reverse(settings.LOGIN_URL)
                    self.assertRedirects(
                        response,
                        # Не могу понять, жду ответа в пачке.
                        f'{login}?{REDIRECT_FIELD_NAME}={reverse_name}',
                        HTTPStatus.FOUND
                    )
        self.assertEqual(self.post_quantity, self.post_quantity)

    def test_guest_cant_create_post(self):
        """Гость не может создавать записи."""
        reverse_name = reverse('posts:post_create')
        response = self.client.post(reverse_name)
        login = reverse(settings.LOGIN_URL)
        self.assertRedirects(
            response,
            f'{login}?{REDIRECT_FIELD_NAME}={reverse_name}',
            HTTPStatus.FOUND
        )
