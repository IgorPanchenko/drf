from django.test import TestCase

from api.serializers import BookSerializer
from books.models import Book


class BookSerializerTestCase(TestCase):
    def test_serializer(self):
        book1 = Book.objects.create(name='Три мушкетера', price=600)
        book2 = Book.objects.create(name='Кот в сапогах', price=200)
        check_data = BookSerializer([book1, book2], many=True).data
        desired_result = [
            {
                'id': book1.id,
                'name': 'Три мушкетера',
                'price': '600.00'
            },
            {
                'id': book2.id,
                'name': 'Кот в сапогах',
                'price': '200.00'
            }
        ]
        self.assertEqual(check_data, desired_result)
