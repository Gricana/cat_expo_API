from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_view_description(self, html=False):
        return 'Создание нового пользователя в системе'
