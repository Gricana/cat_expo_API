from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import \
    JWTStatelessUserAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.models import TokenUser


class CustomJWTStatelessUserAuthentication(JWTStatelessUserAuthentication):
    def authenticate(self, request):
        authenticated_user = super().authenticate(request)
        if authenticated_user is None:
            return None

        user, token = authenticated_user

        if isinstance(user, TokenUser):
            try:
                user = User.objects.get(id=user.id)
            except User.DoesNotExist:
                raise InvalidToken('User not found')

        return user, token
