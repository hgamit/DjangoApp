from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from delivery.models import UserAddress
from delivery.views import UserAddressUpdateView


class UserAddressUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `UserAddressUpdateView` view tests
    '''
    def setUp(self):
        #self.board = Board.objects.create(name='Django', description='Django board.')
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

        self.url = reverse('delivery:edit_useraddress', kwargs={'address_pk': self.useraddress.pk})
        #self.url = reverse('boards:edit_post', kwargs={
        #     'pk': self.board.pk,
        #     'topic_pk': self.topic.pk,
        #     'post_pk': self.post.pk
        # })


class LoginRequiredUserAddressUpdateViewTests(UserAddressUpdateViewTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


# class UnauthorizedUserAddressUpdateViewTests(UserDetailUpdateViewTestCase):
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


class UserAddressUpdateViewTests(UserAddressUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/delivery/1/edit_useraddress/')
        self.assertEquals(view.func.view_class, UserAddressUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 11)
        self.assertContains(self.response, '<select', 1)

class SuccessfulUserAddressUpdateViewTests(UserAddressUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        data = {
            'po_box_number': '100',
            'address_type': 'Communication',
            'street_number': '2171',
            'route': 'Grand Avenue',
            'city': 'Saint Paul',
            'state': 'MN',
            'country': 'United States',
            'zip_code': '55105',
            'point_of_contact': 'john doe',
            'contact_phone': '+16512141111',
        }
        self.response = self.client.post(self.url, data)

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        display_useraddress_url = reverse('delivery:display_useraddress')
        self.assertRedirects(self.response, display_useraddress_url)

    def test_useraddress_changed(self):
        self.useraddress.refresh_from_db()
        self.assertEquals(self.useraddress.po_box_number, '100')
        self.assertEquals(self.useraddress.address_type, 'Communication')
        self.assertEquals(self.useraddress.street_number, '2171')
        self.assertEquals(self.useraddress.route, 'Grand Avenue')
        self.assertEquals(self.useraddress.city, 'Saint Paul')
        self.assertEquals(self.useraddress.state, 'MN')
        self.assertEquals(self.useraddress.country, 'United States')
        self.assertEquals(self.useraddress.zip_code, '55105')
        self.assertEquals(self.useraddress.point_of_contact, 'john doe')
        self.assertEquals(self.useraddress.contact_phone, '+16512141111')


class InvalidUserAddressUpdateViewTests(UserAddressUpdateViewTestCase):
    def setUp(self):
        '''
        Submit an empty dictionary to the `update` view
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