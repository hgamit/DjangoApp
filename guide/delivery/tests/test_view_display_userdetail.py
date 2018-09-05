from django.test import TestCase
from django.urls import reverse, resolve
from delivery.views import UserDetailDisplay
from django.contrib.auth.models import User
from delivery.models import UserDetail

class UserDetailDisplayViewTestCase(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        #self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.userdetail = UserDetail.objects.create(customer=user, user_pic='image.jpg', phone_number='+16512143456', sex='Male', date_of_birth= '1991-01-01')
        self.url = reverse('delivery:display_userdetail')


class UserDetailDisplayViewTests(UserDetailDisplayViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/display_userdetail/')
        self.assertEquals(view.func.view_class, UserDetailDisplay)

    def test_display_userdetail_view_contains_link_back_to_homepage(self):
        homepage_url = reverse('boards:home')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))

    def test_display_userdetail_view_contains_navigation_links(self):
        homepage_url = reverse('boards:home')
        edit_userdetail_url = reverse('delivery:edit_userdetail')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))
        self.assertContains(self.response, 'href="{0}"'.format(edit_userdetail_url))


class LoginRequiredUserDetailDisplayViewTests(UserDetailDisplayViewTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
