from pytest import raises
from rest_framework.exceptions import ValidationError

from api.models import Rating
from api.serializers import CatSerializer, CatRatingSerializer
from .fixtures import *


@pytest.mark.django_db
class TestCatSerializer:
    def test_create_cat(self, owner: User, breed: Breed, color: Color) -> None:
        """Тест создания кота с валидными данными."""
        data = {
            'breed': breed.name,
            'color': color.name,
            'age': 3,
            'description': 'Милый кот',
        }
        serializer = CatSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        created_cat = serializer.save(owner=owner)
        assert created_cat.breed.name == 'Сиамская'
        assert created_cat.color.name == 'Черный'
        assert created_cat.owner == owner

    def test_update_cat(self, cat: Cat) -> None:
        """Тест обновления кота."""
        data = {
            'breed': 'Бенгальская',
            'color': 'Серебристый',
            'age': 4,
            'description': 'Обновленный кот',
        }
        serializer = CatSerializer(instance=cat, data=data, partial=True)
        assert serializer.is_valid()
        updated_cat = serializer.save(owner=cat.owner)
        assert updated_cat.breed.name == 'Бенгальская'
        assert updated_cat.color.name == 'Серебристый'

    def test_average_rating(self, cat: Cat, owner: User, user: User) -> None:
        """Тест вычисления среднего рейтинга кота."""
        Rating.objects.create(cat=cat, user=owner, rating=4)
        Rating.objects.create(cat=cat, user=user, rating=5)

        serializer = CatSerializer(cat)
        assert serializer.data['average_rating'] == 4.5

    def test_cat_rating_validation_by_owner(
            self, cat: Cat, owner: User, req_owner: Request
    ) -> None:
        """Тест проверки валидации: нельзя оценивать собственных котов."""
        data = {'cat': cat.id, 'rating': 3}
        serializer = CatRatingSerializer(
            data=data,
            context={'request': req_owner, 'cat': cat}
        )

        assert not serializer.is_valid()
        with raises(ValidationError) as excinfo:
            serializer.validate(data)
        assert 'Нельзя оценивать собственного котёнка <3' in str(excinfo.value)

    def test_cat_rating_validation_unique(
            self, cat: Cat, req_user: Request
    ) -> None:
        """Тест проверки валидации: нельзя ставить повторные оценки."""
        Rating.objects.create(cat=cat, user=req_user.user, rating=5)
        data = {'cat': cat.id, 'rating': 5}
        serializer = CatRatingSerializer(
            data=data,
            context={'request': req_user, 'cat': cat}
        )

        assert not serializer.is_valid()
        with raises(ValidationError) as excinfo:
            serializer.validate(data)
        assert 'Вижу, что ты меня переоцениваешь. meow..' in str(excinfo.value)
