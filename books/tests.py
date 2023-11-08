from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    def setUpTestData():
        Book.objects.create(name="Pride and Prejudice",
                            genre="classic", book_type="hardcover", price="23.71")

    def test_book_name(self):
        book = Book.objects.get(id=1)

        field_label = book._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_get_absolute_url(self):
       book = Book.objects.get(id=1)
       self.assertEqual(book.get_absolute_url(), '/books/list/1')
