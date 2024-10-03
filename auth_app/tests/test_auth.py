import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestAuthViews:
    client = APIClient()

    def test_register_user(self):
        """
        Тест для регистрации нового пользователя.
        """
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='newuser').exists()

    def test_register_user_with_existing_username(self):
        """
        Тест для попытки регистрации с уже существующим именем пользователя.
        """
        User.objects.create_user(username='newuser', password='password123',
                                 email='newuser@example.com')
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'password123',
            'email': 'anotheremail@example.com'
        }
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'username' in response.data

    def test_obtain_token(self):
        """
        Тест для получения JWT-токена по правильным учетным данным.
        """
        User.objects.create_user(username='testuser', password='testpassword',
                                 email='testuser@example.com')
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_obtain_token_invalid_credentials(self):
        """
        Тест для проверки некорректных учетных данных при получении JWT-токена.
        """
        url = reverse('token_obtain_pair')
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_token(self):
        """
        Тест для обновления access токена
        с использованием валидного refresh токена.
        """
        User.objects.create_user(username='testuser', password='testpassword',
                                 email='testuser@example.com')
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        refresh_token = response.data['refresh']

        refresh_url = reverse('token_refresh')
        response = self.client.post(refresh_url,
                                    {'refresh': refresh_token}, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data

    def test_refresh_token_invalid(self):
        """
        Тест для попытки обновления access токена с невалидным refresh токеном.
        """
        refresh_url = reverse('token_refresh')
        response = self.client.post(refresh_url, {'refresh': 'invalid_token'},
                                    format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
