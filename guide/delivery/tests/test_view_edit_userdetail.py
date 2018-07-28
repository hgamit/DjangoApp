from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from delivery.models import UserDetail
from delivery.views import UserDetailUpdateView


class UserDetailUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        #self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        #self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.userdetail = UserDetail.objects.create(customer=user, user_pic='image.jpg', phone_number='+16512143456', sex='Male', date_of_birth= '1991-01-01')
        self.url = reverse('delivery:edit_userdetail')
        #self.url = reverse('boards:edit_post', kwargs={
        #     'pk': self.board.pk,
        #     'topic_pk': self.topic.pk,
        #     'post_pk': self.post.pk
        # })


class LoginRequiredUserDetailUpdateViewTests(UserDetailUpdateViewTestCase):
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


class UserDetailUpdateViewTests(UserDetailUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/edit_userdetail/')
        self.assertEquals(view.func.view_class, UserDetailUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, '<select', 1)


class SuccessfulUserDetailUpdateViewTests(UserDetailUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        data = {
            'user_pic': 'image.jpg',
            'phone_number': '+16512143456',
            'sex': 'Male',
            'date_of_birth': '1991-01-01'
        }
        self.response = self.client.post(self.url, data)

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        display_userdetail_url = reverse('delivery:display_userdetail')
        self.assertRedirects(self.response, display_userdetail_url)

    def test_userdetail_changed(self):
        self.userdetail.refresh_from_db()
        self.assertEquals(self.userdetail.user_pic, 'image.jpg')
        self.assertEquals(self.userdetail.phone_number, '+16512143456')
        self.assertEquals(self.userdetail.sex, 'Male')
        self.assertEquals(self.userdetail.date_of_birth, datetime.date(1991, 1, 1))


class InvalidUserDetailUpdateViewTests(UserDetailUpdateViewTestCase):
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