from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data: dict) -> User:
        """
        Метод для создания нового пользователя.
        Пароль автоматически хэшируется.

        Аргументы:
            validated_data (dict): Валидированные данные.

        Возвращает:
            User: Созданный экземпляр пользователя.
        """
        user = User.objects.create_user(**validated_data)
        return user
