from django.db import models
from django.shortcuts import reverse

genre_choices = (('classic', 'Classic'),
                 ('classic', 'Classic'),
                 ('romantic', 'Romantic'),
                 ('comic', 'Comic'),
                 ('fantasy', 'Fantasy'),
                 ('horror', 'Horror'),
                 ('educational', 'Educational'))

book_type_choices = (
    ('hardcover', 'Hardcover'),
    ('ebook', 'E-book'),
    ('audiobook', 'Audiobook')
)


class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120, default="not specified")
    price = models.FloatField(help_text='in US dollars $')
    genre = models.CharField(
        max_length=12, choices=genre_choices, default='classic')
    book_type = models.CharField(
        max_length=12, choices=book_type_choices, default='hardcover')
    pic = models.ImageField(upload_to='books', default='book.png')

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)
