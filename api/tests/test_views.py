import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Breed, Cat, Color, Rating
from .fixtures import auth_client, auth_client_by_owner, owner, user


@pytest.mark.django_db
class TestCatViewSet:

    @pytest.fixture(autouse=True)
    def setup(self, owner: User, user: User) -> None:
        """Настройка объектов перед тестами."""
        self.owner = owner
        self.user = user

        self.breed = Breed.objects.create(name='Сиамская')
        self.breed_1 = Breed.objects.create(name='Бенгальская')
        self.color = Color.objects.create(name='Черный')
        self.color_1 = Color.objects.create(name='Серебристый')

        self.cat = Cat.objects.create(
            owner=self.owner,
            breed=self.breed,
            color=self.color,
            age=12,
            description='Красивая кошка'
        )

        self.cat_1 = Cat.objects.create(
            owner=self.user,
            breed=self.breed_1,
            color=self.color_1,
            age=48,
            description='Красивая кошка'
        )

    def test_list_breeds(self, auth_client: APIClient) -> None:
        """Тест списка пород кошек."""
        url = reverse('breed-list')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_create_cat(self, auth_client: APIClient) -> None:
        """Тест создания нового кота."""
        url = reverse('cats-list')
        data = {
            'breed': 'Мейн-кун',
            'color': 'Дымчатый',
            'age': 6,
            'description': 'Милый кот'
        }
        response = auth_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Cat.objects.count() == 3

    def test_get_cat(self, auth_client: APIClient) -> None:
        """Тест получения информации о конкретном коте."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.cat.id

    def test_rate_cat_by_user(self, auth_client: APIClient) -> None:
        """Тест добавления оценки коту пользователем."""
        url = reverse('cats-rate', kwargs={'pk': self.cat.id})
        data = {'rating': 5}

        initial_rating_count = Rating.objects.filter(cat=self.cat).count()
        response = auth_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        new_rating_count = Rating.objects.filter(cat=self.cat).count()
        assert new_rating_count == initial_rating_count + 1

    def test_rate_cat_by_owner(self, auth_client_by_owner: APIClient) -> None:
        """Тест: владелец не может оценивать своего кота."""
        url = reverse('cats-rate', kwargs={'pk': self.cat.id})
        data = {'rating': 4}
        response = auth_client_by_owner.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'non_field_errors' in response.data
        assert response.data['non_field_errors'][0].code == 'invalid'
        assert (str(response.data['non_field_errors'][0])
                == 'Нельзя оценивать собственного котёнка <3')

    def test_rate_cat_invalid(self, auth_client: APIClient) -> None:
        """Тест: проверка недопустимого значения оценки."""
        url = reverse('cats-rate', kwargs={'pk': self.cat.id})
        data = {'rating': -4.7}
        response = auth_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'rating' in response.data
        assert response.data['rating'][0].code == 'invalid'
        assert str(
            response.data['rating'][0]) == 'A valid integer is required.'

    def test_get_cats_by_breed(self, auth_client: APIClient) -> None:
        """Тест получения котов по породе."""
        url = reverse('cats-list') + f'?breed_id={self.breed.id}'
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_list_cats_anonymous(self) -> None:
        """Тест получения списка котов анонимным пользователем."""
        url = reverse('cats-list')
        client = APIClient()
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_update_cat_by_owner(self, auth_client_by_owner: APIClient) \
            -> None:
        """Тест обновления кота владельцем."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        data = {
            'breed': 'Сиамская',
            'color': 'Серо-голубой',
            'age': 5,
            'description': 'Обновлённая кошка'
        }

        response = auth_client_by_owner.put(url, data, format='json')

        assert response.status_code == status.HTTP_200_OK
        self.cat.refresh_from_db()
        assert Color.objects.get(name='Серо-голубой')
        assert self.cat.breed.name == Breed.objects.get(name='Сиамская').name
        assert self.cat.age == 5

    def test_update_cat_by_non_owner(self, auth_client: APIClient) -> None:
        """Тест: пользователь не может обновлять кота, если он не владелец."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        data = {
            'breed': 'Бенгальская',
            'color': 'Серебристый',
            'age': 5,
            'description': 'Описание обновленной кошки'
        }

        response = auth_client.put(url, data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_cat_by_owner(self,
                                 auth_client_by_owner: APIClient) -> None:
        """Тест удаления кота владельцем."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        response = auth_client_by_owner.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Cat.objects.filter(id=self.cat.id).count() == 0

    def test_delete_cat_by_non_owner(self, auth_client: APIClient) -> None:
        """Тест: пользователь не может удалять кота, если он не владелец."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        response = auth_client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_cat_anonymous(self) -> None:
        """Тест: анонимный пользователь не может создать кота."""
        url = reverse('cats-list')
        data = {
            'breed': 'Мейн-кун',
            'color': 'Дымчатый',
            'age': 6,
            'description': 'Милый кот'
        }
        client = APIClient()
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_rate_cat_anonymous(self) -> None:
        """Тест: анонимный пользователь не может оценивать котов."""
        url = reverse('cats-rate', kwargs={'pk': self.cat.id})
        data = {'rating': 5}
        client = APIClient()
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_cat_anonymous(self) -> None:
        """Тест: анонимный пользователь не может обновлять кота."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        data = {
            'breed': 'Бенгальская',
            'color': 'Серебристый',
            'age': 5,
            'description': 'Обновленная кошка'
        }
        client = APIClient()
        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_cat_anonymous(self) -> None:
        """Тест: анонимный пользователь не может удалять кота."""
        url = reverse('cats-detail', kwargs={'pk': self.cat.id})
        client = APIClient()
        response = client.delete(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_nonexistent_cat(self, auth_client: APIClient) -> None:
        """Тест: запрос несуществующего кота возвращает 404."""
        url = reverse('cats-detail', kwargs={'pk': 952})
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
