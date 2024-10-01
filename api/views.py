from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from rest_framework.response import Response

from .api_desc import operation_descriptions
from .models import Breed, Cat
from .permissions import IsOwnerOrReadOnly
from .serializers import BreedSerializer, CatSerializer, CatRatingSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    @swagger_auto_schema(
        operation_description="Получение всех пород кошек, "
                              "представленных на выставке",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        breed_id = self.request.query_params.get('breed_id')
        if breed_id:
            return Cat.objects.filter(breed_id=breed_id)
        return CatViewSet.queryset

    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated])
    @swagger_auto_schema(request_body=CatRatingSerializer, )
    def rate(self, request, pk=None):
        cat = self.get_object()
        serializer = CatRatingSerializer(data=request.data,
                                         context={'request': request,
                                                  'cat': cat})
        if serializer.is_valid():
            serializer.save(cat=cat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Applying API descriptions to each viewset method
for method, description in operation_descriptions.items():
    setattr(CatViewSet, method,
            swagger_auto_schema(operation_description=description)(
                getattr(CatViewSet, method)))
