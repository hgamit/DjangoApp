from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from delivery.forms import UserSecurityInfoForm
from delivery.models import UserSecurityInfo
from delivery.views import new_securityinfo


class NewUserSecurityInfoTests(TestCase):
    
    def setUp(self):
        #Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')
        self.url = reverse('delivery:new_securityinfo')

    def test_new_securityinfo_view_success_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    # def test_new_userdetail_view_not_found_status_code(self):
    #     url = reverse('boards:new_topic', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    def test_new_securityinfo_url_resolves_new_topic_view(self):
        view = resolve('/delivery/new_securityinfo/')
        self.assertEquals(view.func, new_securityinfo)

    def test_new_securityinfo_view_contains_link_back_to_board_home_view(self):
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
        self.assertIsInstance(form, UserSecurityInfoForm)

    def test_new_securityinfo_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        data = {
            'ssn_number': '', 
            'ssn_img': '', 
            'dl_state': '',  
            'dl_number': '', 
            'dlside1_img': '', 
            'dlside2_img': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(UserSecurityInfo.objects.exists())
        #self.assertFalse(Post.objects.exists())


    def test_new_securityinfo_valid_post_data(self):
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        data = {
            'ssn_number': '714238324', 
            'ssn_img': 'ssn.jpg', 
            'dl_state': 'MN',  
            'dl_number': 'M263634281411', 
            'dlside1_img': 'dlside1_img.jpg', 
            'dlside2_img': 'dlside2_img.jpg'
        }
        self.client.post(self.url, data)
        self.assertTrue(UserSecurityInfo.objects.exists())
        #self.assertTrue(Post.objects.exists())

    def test_new_securityinfo_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        #url = reverse('boards:new_topic', kwargs={'pk': 1})
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)


class LoginRequiredUserSecurityInfoTests(TestCase):
    def setUp(self):
        #Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('delivery:new_securityinfo')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('accounts:login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))