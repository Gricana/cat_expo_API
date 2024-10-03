from django.db.models import Avg
from rest_framework import serializers

from .models import Breed, Cat, Rating, Color


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для породы кошек.
    """

    class Meta:
        model = Breed
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """
    Сериализатор для оценок котов.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'user',)


class CatSerializer(serializers.ModelSerializer):
    """
    Сериализатор для котов. Включает в себя поля для породы, цвета,
    владельца, среднего рейтинга и всех оценок.
    """
    breed = serializers.CharField(
        max_length=100, help_text="Порода кошки"
    )
    color = serializers.CharField(
        max_length=30, help_text="Цвет кошки"
    )
    owner = serializers.ReadOnlyField(
        source='owner.username', help_text="Владелец кошки"
    )
    average_rating = serializers.SerializerMethodField(
        help_text="Средний рейтинг"
    )
    ratings = RatingSerializer(
        many=True, read_only=True, help_text="Оценки пользователей"
    )

    class Meta:
        model = Cat
        fields = '__all__'

    def get_average_rating(self, obj) -> float:
        """
        Метод для вычисления среднего рейтинга кота.

        :param obj: Объект кота.
        :return: Средний рейтинг или None, если оценок нет.
        """
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(ratings.aggregate(Avg('rating'))['rating__avg'], 2)
        return None

    def create(self, validated_data) -> Cat:
        """
        Метод создания нового кота с обработкой названий породы и цвета.

        :param validated_data: Валидационные данные.
        :return: Созданный объект Cat.
        """
        breed_name = validated_data.pop('breed')
        color_name = validated_data.pop('color')

        breed, _ = Breed.objects.get_or_create(name=breed_name)
        color, _ = Color.objects.get_or_create(name=color_name)

        validated_data['breed'] = breed
        validated_data['color'] = color

        return Cat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Метод обновления кота с возможностью изменения породы и цвета.

        :param instance: Существующий объект кота.
        :param validated_data: Валидационные данные.
        :return: Обновленный объект Cat.
        """
        if 'breed' in validated_data:
            breed_name = validated_data.pop('breed')
            breed, _ = Breed.objects.get_or_create(name=breed_name)
            instance.breed = breed

        if 'color' in validated_data:
            color_name = validated_data.pop('color')
            color, _ = Color.objects.get_or_create(name=color_name)
            instance.color = color

        return super().update(instance, validated_data)


class CatRatingSerializer(serializers.ModelSerializer):
    """
    Сериализатор для оценки котов.
    """
    cat = CatSerializer(many=False, read_only=True)

    class Meta:
        model = Rating
        fields = ('cat', 'rating',)

    def validate(self, data):
        """
        Метод валидации для оценки кота. Владелец не может оценивать
        своего кота, а повторная оценка невозможна.

        :param data: Валидационные данные.
        :return: Валидированные данные или ошибка валидации.
        """
        cat = self.context['cat']
        user = self.context['request'].user

        if cat.owner == user:
            raise serializers.ValidationError(
                'Нельзя оценивать собственного котёнка <3'
            )

        if Rating.objects.filter(cat=cat, user=user).exists():
            raise serializers.ValidationError(
                "Вижу, что ты меня переоцениваешь. meow.."
            )

        return data

    def create(self, validated_data) -> Rating:
        """
        Метод создания оценки кота.

        :param validated_data: Валидационные данные.
        :return: Созданный объект Rating.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
