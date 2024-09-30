from django.db.models import Avg
from rest_framework import serializers

from .models import Breed, Cat, Rating


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
    owner = serializers.ReadOnlyField(source='owner.username')
    average_rating = serializers.SerializerMethodField()
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(ratings.aggregate(Avg('rating'))['rating__avg'], 2)
        return None


class CatRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('cat', 'rating',)

    def validate(self, data):
        if data['cat'].owner == self.context['request'].user:
            raise serializers.ValidationError('Нельзя оценивать своего '
                                              'собственного котёнка <3')
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
