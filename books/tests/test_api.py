from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase

from api.serializers import BookSerializer
from books.models import Book


class BooksApiTestCase(APITestCase):
    def test_get_list(self):
        book1 = Book.objects.create(name='Три мушкетера', price=600)
        book2 = Book.objects.create(name='Кот в сапогах', price=200)
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([book1, book2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
