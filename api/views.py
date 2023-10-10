from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import BookSerializer
from books.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer