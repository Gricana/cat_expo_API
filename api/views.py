from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from rest_framework.response import Response

from .models import Breed, Cat
from .permissions import IsOwnerOrReadOnly
from .serializers import BreedSerializer, CatSerializer, CatRatingSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        breed_id = self.request.query_params.get('breed_id')
        if breed_id:
            return Cat.objects.filter(breed_id=breed_id)
        return CatViewSet.queryset

    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated])
    def rate(self, request, pk=None):
        cat = self.get_object()
        serializer = CatRatingSerializer(data=request.data,
                                         context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(cat=cat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
