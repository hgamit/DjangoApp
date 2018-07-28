from django.test import TestCase
from django.urls import reverse, resolve
from delivery.views import UserSecurityInfoDisplay
from django.contrib.auth.models import User
from delivery.models import UserSecurityInfo

class UserSecurityInfoDisplayViewTestCase(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        #self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.usersecurityinfo = UserSecurityInfo.objects.create(customer=user, ssn_number='714238324', ssn_img='ssn.jpg', dl_state='MN', dl_number= 'M263634281411', dlside1_img='dlside1_img.jpg', dlside2_img= 'dlside2_img.jpg')
        self.url = reverse('delivery:display_securityinfo')


class UserSecurityInfoDisplayViewTests(UserSecurityInfoDisplayViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/display_securityinfo/')
        self.assertEquals(view.func.view_class, UserSecurityInfoDisplay)

    def test_display_securityinfo_view_contains_link_back_to_homepage(self):
        homepage_url = reverse('boards:home')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))

    def test_display_securityinfo_view_contains_navigation_links(self):
        homepage_url = reverse('boards:home')
        edit_securityinfo_url = reverse('delivery:edit_securityinfo')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))
        self.assertContains(self.response, 'href="{0}"'.format(edit_securityinfo_url))


class LoginRequiredUserSecurityInfoDisplayViewTests(UserSecurityInfoDisplayViewTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
