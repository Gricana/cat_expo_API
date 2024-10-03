from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import \
    JWTStatelessUserAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.models import TokenUser


class CustomJWTStatelessUserAuthentication(JWTStatelessUserAuthentication):
    """
    Класс аутентификации, использующий JWT с проверкой на существование пользователя.
    Если пользователь не найден, выбрасывается исключение InvalidToken.
    """

    def authenticate(self, request):
        """
        Переопределенный метод аутентификации,
        который проверяет, существует ли пользователь,
        связанный с классом TokenUser.
        Если пользователь не найден, выбрасывается InvalidToken.

        Возвращает:
            tuple: Кортеж, содержащий пользователя и токен,
            если аутентификация успешна.
            Иначе возвращает None.
        """
        authenticated_user = super().authenticate(request)
        if authenticated_user is None:
            return None

        user, token = authenticated_user

        if isinstance(user, TokenUser):
            try:
                user = User.objects.get(id=user.id)
            except User.DoesNotExist:
                raise InvalidToken('Пользователь не найден')

        return user, token
