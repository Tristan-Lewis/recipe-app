from django.db import models
from django.shortcuts import reverse

difficulty_choices = (('easy', 'Easy'),
                      ('medium', 'Medium'),
                      ('intermediate', 'Intermediate'),
                      ('hard', 'Hard'))

# Create your models here.


class Recipe(models.Model):
    __tablename__ = "final_recipes"
    name = models.CharField(max_length=20)
    ingredients = models.TextField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    difficulty = models.CharField(max_length=12, choices=difficulty_choices)
    pic = models.ImageField(upload_to='food' , default='book.png')

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if len(self.ingredients == 0):
            return []
        else:
            return self.ingredients.split(", ")
