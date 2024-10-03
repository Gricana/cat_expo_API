from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from rest_framework.response import Response

from .api_desc import operation_descriptions
from .models import Breed, Cat
from .permissions import IsOwnerOrReadOnly
from .serializers import BreedSerializer, CatSerializer, CatRatingSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для просмотра пород кошек. Доступен только для чтения.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    @swagger_auto_schema(
        operation_description=operation_descriptions['list'],
    )
    def list(self, request, *args, **kwargs):
        """
        Получение списка всех пород кошек.
        """
        return super().list(request, *args, **kwargs)


class CatViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления котами.
    Включает создание, обновление, удаление и рейтинг котов.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @swagger_auto_schema(
        operation_description=operation_descriptions['create']
    )
    def perform_create(self, serializer):
        """
        Автоматически добавляет владельца (пользователя) к создаваемому коту.
        """
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(
        operation_description=operation_descriptions['list']
    )
    def get_queryset(self):
        """
        Возвращает всех котов или фильтрует их по породе.
        """
        breed_id = self.request.query_params.get('breed_id')
        if breed_id:
            return Cat.objects.filter(breed_id=breed_id)
        return CatViewSet.queryset

    @swagger_auto_schema(
        request_body=CatRatingSerializer,
        operation_description=operation_descriptions['rate']
    )
    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated])
    def rate(self, request, pk=None):
        """
        Метод для оценки кота. Только аутентифицированные пользователи
        могут оценивать котов.
        """
        cat = self.get_object()
        serializer = CatRatingSerializer(data=request.data,
                                         context={'request': request,
                                                  'cat': cat})
        if serializer.is_valid():
            serializer.save(cat=cat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
