from django.urls import resolve, reverse
from django.test import TestCase
from delivery.views import getdetails
from django.contrib.auth.models import User
from delivery.models import UserDetail
from delivery.forms import UserDetailForm


class GetdetailsTests(TestCase):
    def setUp(self):
        url = reverse('delivery:getdetails')
        self.response = self.client.get(url)
        User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_getdetails_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_getdetails_url_resolves_getdetails_view(self):
        view = resolve('/delivery/getdetails/')
        self.assertEquals(view.func, getdetails)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('delivery:getdetails')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'sex': 'Male',
            'date_of_birth': '1991-01-01'
        }
        response = self.client.post(url, data)
        self.assertTrue(UserDetail.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('delivery:getdetails')
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_contains_form(self):  # <- new test
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserDetailForm)

    def test_getdetails_invalid_post_data(self):  # <- updated this one
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('delivery:getdetails')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)