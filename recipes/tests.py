from django.test import TestCase
from .models import Recipe


class RecipeModelTest(TestCase):
# Create your tests here.
    def setUpTestData():
        Recipe.objects.create(name="Scrambled Eggs",
                            ingredients="Eggs", cooking_time="5", difficulty="Easy")

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)

        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def RecipeFormTestl(self):
       recipe = Recipe.objects.get(id=1)
       self.assertEqual(recipe.get_absolute_url(), '/recipe/1')


