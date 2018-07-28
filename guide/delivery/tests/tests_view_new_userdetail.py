from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from delivery.forms import UserDetailForm
from delivery.models import UserDetail
from delivery.views import new_userdetail


class NewUserDetailTests(TestCase):

    def setUp(self):
        #Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')
        self.url = reverse('delivery:new_userdetail')

    def test_new_userdetail_view_success_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    # def test_new_userdetail_view_not_found_status_code(self):
    #     url = reverse('boards:new_topic', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    def test_new_userdetail_url_resolves_new_topic_view(self):
        view = resolve('/delivery/new_userdetail/')
        self.assertEquals(view.func, new_userdetail)

    def test_new_userdetail_view_contains_link_back_to_board_home_view(self):
        #new_userdetail_url = reverse('delivery:new_userdetail')
        board_home_url = reverse('boards:home',)
        response = self.client.get(self.url)
        self.assertContains(response, 'href="{0}"'.format(board_home_url))

    def test_csrf(self):
        #url = reverse('delivery:new_userdetail')
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        #url = reverse('delivery:new_userdetail')
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, UserDetailForm)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        data = {
            'user_pic': '',
            'phone_number': '',
            'sex': '',
            'date_of_birth': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(UserDetail.objects.exists())
        #self.assertFalse(Post.objects.exists())


    def test_new_topic_valid_post_data(self):
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        data = {
            'user_pic': 'image.jpg',
            'phone_number': '+16512143456',
            'sex': 'Male',
            'date_of_birth': '1991-01-01'
        }
        self.client.post(self.url, data)
        self.assertTrue(UserDetail.objects.exists())
        #self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)


class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        #Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('delivery:new_userdetail')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('accounts:login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))