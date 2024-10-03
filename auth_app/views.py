from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    Представление для регистрации нового пользователя.
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_view_description(self, html: bool = False) -> str:
        """
        Метод для предоставления пользовательского описания действия.
        """
        return 'Создание нового пользователя в системе'
