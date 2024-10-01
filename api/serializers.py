from django.db.models import Avg
from rest_framework import serializers

from .models import Breed, Cat, Rating, Color


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'user',)


class CatSerializer(serializers.ModelSerializer):
    breed = serializers.CharField(max_length=100, help_text="Порода кошки")
    color = serializers.CharField(max_length=30, help_text="Цвет кошки")
    owner = serializers.ReadOnlyField(source='owner.username',
                                      help_text="Владелец кошки")
    average_rating = serializers.SerializerMethodField(
        help_text="Средний рейтинг")
    ratings = RatingSerializer(many=True, read_only=True,
                               help_text="Оценки пользователей")

    class Meta:
        model = Cat
        fields = '__all__'

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(ratings.aggregate(Avg('rating'))['rating__avg'], 2)
        return None

    def create(self, validated_data):
        breed_name = validated_data.pop('breed')
        color_name = validated_data.pop('color')

        breed, created = Breed.objects.get_or_create(name=breed_name)
        color, created = Color.objects.get_or_create(name=color_name)

        validated_data['breed'] = breed
        validated_data['color'] = color

        return Cat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if ('breed', 'color') in validated_data:
            breed_name = validated_data.pop('breed')
            color_name = validated_data.pop('color')

            breed, created = Breed.objects.get_or_create(name=breed_name)
            color, created = Color.objects.get_or_create(name=color_name)

            instance.breed = breed
            instance.color = color

        return super().update(instance, validated_data)


class CatRatingSerializer(serializers.ModelSerializer):
    cat = CatSerializer(many=False, read_only=True)

    class Meta:
        model = Rating
        fields = ('cat', 'rating',)

    def validate(self, data):
        cat = self.context['cat']
        user = self.context['request'].user

        if self.context['cat'].owner == self.context['request'].user:
            raise serializers.ValidationError('Нельзя оценивать своего '
                                              'собственного котёнка <3')

        if Rating.objects.filter(cat=cat, user=user).exists():
            raise serializers.ValidationError(
            "Вижу, что ты меня переоцениваешь. meow...")

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
