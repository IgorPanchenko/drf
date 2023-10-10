from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import BookSerializer
from books.models import Book
from books.permissions import IsOwnerAuthenticatedOrReadOnly


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['price']
    search_fields = ('name', 'author')
    ordering_fields = ['price', 'author']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
