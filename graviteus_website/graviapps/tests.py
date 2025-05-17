from django.test import TestCase
from django.contrib.auth.models import User
from graviapps.models import UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfileTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='jora', password='pass123')

    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(user=self.user)
        self.assertEqual(profile.user.username, 'jora')

    def test_user_profile_default_avatar(self):
        profile = UserProfile.objects.create(user=self.user)
        self.assertIsNotNone(profile.avatar)

    def test_user_profile_str(self):
        profile = UserProfile.objects.create(user=self.user)
        self.assertEqual(str(profile), 'jora')

    def test_user_profile_custom_avatar(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'fake image content', content_type='image/jpeg')
        profile = UserProfile.objects.create(user=self.user, avatar=image)
        self.assertTrue(profile.avatar.name.endswith('test_image.jpg'))

    def test_user_profile_fields_exist(self):
        profile = UserProfile.objects.create(user=self.user)
        self.assertTrue(hasattr(profile, 'avatar'))
        self.assertTrue(hasattr(profile, 'bio'))


class ViewAccessTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewer', password='viewerpass')

    def test_homepage_access(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_profile_access_denied(self):
        # доступ к профилю без входа
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # редирект на логин

    def test_profile_access_authenticated(self):
        self.client.login(username='viewer', password='viewerpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_redirects(self):
        self.client.login(username='viewer', password='viewerpass')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
