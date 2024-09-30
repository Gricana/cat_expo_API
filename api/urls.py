from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import BreedViewSet, CatViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'breeds', BreedViewSet)
router.register(r'cats', CatViewSet, basename='cats')

schema_view = get_schema_view(
    openapi.Info(
        title="Cat expo API",
        default_version='v1',
        description="Cat Expo API Documentation",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(name="API Support",
                                email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    # API routes
    path('', include(router.urls)),
    # Swagger docs routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
