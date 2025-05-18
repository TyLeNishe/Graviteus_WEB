from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class SimpleViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    # --- 10 базовых тестов страниц ---
    def test_home_page(self): self.assertEqual(self.client.get(reverse('home')).status_code, 200)
    def test_about_page(self): self.assertEqual(self.client.get(reverse('about')).status_code, 200)
    def test_shop_page(self): self.assertEqual(self.client.get(reverse('shop')).status_code, 200)
    def test_lor_page(self): self.assertEqual(self.client.get(reverse('lor')).status_code, 200)
    def test_login_page(self): self.assertEqual(self.client.get(reverse('login')).status_code, 200)
    def test_register_page(self): self.assertEqual(self.client.get(reverse('register')).status_code, 200)
    def test_unknown_page(self): self.assertEqual(self.client.get('/unknown/').status_code, 404)
    def test_profile_redirect(self): self.assertEqual(self.client.get(reverse('profile')).status_code, 302)
    def test_update_email_redirect(self): self.assertEqual(self.client.post(reverse('update_email')).status_code, 302)
    def test_update_username_redirect(self): self.assertEqual(self.client.post(reverse('update_username')).status_code, 302)

    # --- 5 повторов и GET к POST-представлениям ---
    def test_register_page_get_twice(self):
        self.client.get(reverse('register'))
        self.assertEqual(self.client.get(reverse('register')).status_code, 200)

    def test_login_post_with_empty_data(self):
        response = self.client.post(reverse('login'), {})
        self.assertEqual(response.status_code, 200)

    def test_update_email_get(self): self.assertEqual(self.client.get(reverse('update_email')).status_code, 302)
    def test_update_username_get(self): self.assertEqual(self.client.get(reverse('update_username')).status_code, 302)
    def test_delete_account_get(self): self.assertEqual(self.client.get(reverse('delete_account')).status_code, 302)

    # --- 5 проверок HTML-шаблонов ---
    def test_homepage_contains_html(self): self.assertContains(self.client.get(reverse('home')), '<')
    def test_aboutpage_contains_html(self): self.assertContains(self.client.get(reverse('about')), '<html')
    def test_shop_contains_html(self): self.assertContains(self.client.get(reverse('shop')), '<html')
    def test_register_form_in_html(self): self.assertContains(self.client.get(reverse('register')), '<form')
    def test_login_form_in_html(self): self.assertContains(self.client.get(reverse('login')), '<form')


class UserModelTests(TestCase):
    # --- 5 простых тестов User-модели ---
    def test_user_creation(self):
        user = User.objects.create_user(username='alice', password='123')
        self.assertEqual(user.username, 'alice')

    def test_user_duplicate_username(self):
        User.objects.create_user(username='bob', password='123')
        exists = User.objects.filter(username='bob').exists()
        self.assertTrue(exists)

    def test_user_email_field(self):
        user = User.objects.create_user(username='test', email='test@mail.com', password='123')
        self.assertEqual(user.email, 'test@mail.com')

    def test_user_check_password(self):
        user = User.objects.create_user(username='dan', password='secure123')
        self.assertTrue(user.check_password('secure123'))

    def test_user_str_representation(self):
        user = User.objects.create_user(username='human', password='x')
        self.assertEqual(str(user), 'human')