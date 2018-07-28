from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from delivery.models import UserSecurityInfo
from delivery.views import UserSecurityInfoUpdateView


class UserSecurityInfoUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        #self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        #self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.usersecurityinfo = UserSecurityInfo.objects.create(customer=user, ssn_number='714238324', ssn_img='ssn.jpg', dl_state='MN', dl_number= 'M263634281411', dlside1_img='dlside1_img.jpg', dlside2_img= 'dlside2_img.jpg')
        self.url = reverse('delivery:edit_securityinfo')
        #self.url = reverse('boards:edit_post', kwargs={
        #     'pk': self.board.pk,
        #     'topic_pk': self.topic.pk,
        #     'post_pk': self.post.pk
        # })


class LoginRequiredUserSecurityInfoUpdateViewTests(UserSecurityInfoUpdateViewTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


# class UnauthorizedUserDetailUpdateViewTests(UserDetailUpdateViewTestCase):
#     def setUp(self):
#         super().setUp()
#         username = 'jane'
#         password = '321'
#         user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
#         self.client.login(username=username, password=password)
#         self.response = self.client.get(self.url)

#     def test_status_code(self):
#         '''
#         A topic should be edited only by the owner.
#         Unauthorized users should get a 404 response (Page Not Found)
#         '''
#         self.assertEquals(self.response.status_code, 404)


class UserSecurityInfoUpdateViewTests(UserSecurityInfoUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/edit_securityinfo/')
        self.assertEquals(view.func.view_class, UserSecurityInfoUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, '<select', 1)


class SuccessfulUserSecurityInfoUpdateViewTests(UserSecurityInfoUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        data = {
            'ssn_number': '714238324', 
            'ssn_img': 'ssn.jpg', 
            'dl_state': 'MN',  
            'dl_number': 'M263634281411', 
            'dlside1_img': 'dlside1_img.jpg', 
            'dlside2_img': 'dlside2_img.jpg'
        }
        self.response = self.client.post(self.url, data)

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        display_securityinfo_url = reverse('delivery:display_securityinfo')
        self.assertRedirects(self.response, display_securityinfo_url)

    def test_userdetail_changed(self):
        self.usersecurityinfo.refresh_from_db()
        self.assertEquals(self.usersecurityinfo.ssn_number, '714-23-8324')
        self.assertEquals(self.usersecurityinfo.ssn_img, 'ssn.jpg')
        self.assertEquals(self.usersecurityinfo.dl_state, 'MN')
        self.assertEquals(self.usersecurityinfo.dl_number, 'M263634281411')
        self.assertEquals(self.usersecurityinfo.dlside1_img, 'dlside1_img.jpg')
        self.assertEquals(self.usersecurityinfo.dlside2_img, 'dlside2_img.jpg')


class InvalidUserSecurityInfoUpdateViewTests(UserSecurityInfoUpdateViewTestCase):
    def setUp(self):
        '''
        Submit an empty dictionary to the `reply_topic` view
        '''
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)