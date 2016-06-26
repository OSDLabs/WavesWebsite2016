from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from .models import *

class ProfileViewsTestCase(TestCase):
	# fixtures = ['profile_views_testdata.json']

	def setUp(self):
		user = User.objects.create_user('seban', 'sebastinssanty@gmail.com', '123')

	def test_secure_page(self):
		self.client.login(username='seban', password='123')
		response = self.client.get('/profile/', follow=True)
		self.assertEqual(response.status_code, 200)
		user = User.objects.get(username='seban')
		self.assertTrue('form' in response.context)