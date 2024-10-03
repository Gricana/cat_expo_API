from typing import Generator

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserType
from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Breed, Cat, Color

User = get_user_model()


@pytest.fixture
def owner(db) -> Generator[UserType, None, None]:
    """Создает владельца (пользователя)."""
    owner = User.objects.create_user(
        username='testowner',
        password='testpassword',
        email='testowner@example.com'
    )
    yield owner


@pytest.fixture
def user(db) -> Generator[UserType, None, None]:
    """Создает обычного пользователя."""
    user = User.objects.create_user(
        username='testuser',
        password='testpassword',
        email='testuser@example.com'
    )
    yield user


@pytest.fixture
def auth_client(user: UserType) -> Generator[APIClient, None, None]:
    """Создает авторизованный клиент для обычного пользователя."""
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    yield client


@pytest.fixture
def auth_client_by_owner(owner: UserType) -> Generator[APIClient, None, None]:
    """Создает авторизованный клиент для владельца (пользователя)."""
    client = APIClient()
    refresh = RefreshToken.for_user(owner)
    token = str(refresh.access_token)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    yield client


@pytest.fixture
def req_user(user: UserType) -> Generator[Request, None, None]:
    """Создает APIRequestFactory с обычным пользователем."""
    factory = APIRequestFactory()
    request = factory.post('/fake-url/')
    request.user = user
    yield request


@pytest.fixture
def req_owner(owner: UserType) -> Generator[Request, None, None]:
    """Создает APIRequestFactory с владельцем (пользователем)."""
    factory = APIRequestFactory()
    request = factory.post('/fake-url/')
    request.user = owner
    yield request


@pytest.fixture
def breed() -> Generator[Breed, None, None]:
    """Создает объект породы."""
    breed = Breed.objects.create(name='Сиамская')
    yield breed


@pytest.fixture
def color() -> Generator[Color, None, None]:
    """Создает объект цвета."""
    color = Color.objects.create(name='Черный')
    yield color


@pytest.fixture
def cat(owner: UserType, breed: Breed, color: Color) \
        -> Generator[Cat, None, None]:
    """Создает кота для тестов."""
    cat = Cat.objects.create(
        breed=breed,
        color=color,
        age=3,
        description='Милый кот',
        owner=owner
    )
    yield cat
