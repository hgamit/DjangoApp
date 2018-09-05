from django.test import TestCase
from django.urls import reverse, resolve
from delivery.views import UserAddressDisplay
from django.contrib.auth.models import User
from delivery.models import UserAddress

class UserAddressDisplayViewTestCase(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        #self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.useraddress = UserAddress.objects.create(customer=user, 
            po_box_number = '100',
            address_type = 'Communication',
            street_number = '2171',
            route = 'Grand Avenue',
            city = 'Saint Paul',
            state = 'MN',
            country = 'United States',
            zip_code = '55105',
            point_of_contact = 'john doe',
            contact_phone = '+16512141111',)
        self.url = reverse('delivery:display_useraddress')


class UserAddressDisplayViewTests(UserAddressDisplayViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/display_useraddress/')
        self.assertEquals(view.func.view_class, UserAddressDisplay)

    def test_display_useraddress_view_contains_link_back_to_homepage(self):
        homepage_url = reverse('boards:home')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))

    def test_display_useraddress_view_contains_navigation_links(self):
        homepage_url = reverse('boards:home')
        edit_useraddress_url = reverse('delivery:edit_useraddress' , kwargs={'address_pk': self.useraddress.pk})
        delete_useraddress_url = reverse('delivery:delete_useraddress', kwargs={'address_pk': self.useraddress.pk})
        new_useraddress_url = reverse('delivery:new_useraddress')
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))
        self.assertContains(self.response, 'href="{0}"'.format(edit_useraddress_url))
        self.assertContains(self.response, 'href="{0}"'.format(delete_useraddress_url))
        self.assertContains(self.response, 'href="{0}"'.format(new_useraddress_url))


class LoginRequiredUserAddressDisplayViewTests(UserAddressDisplayViewTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
