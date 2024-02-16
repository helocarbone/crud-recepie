from django.test import TestCase

from core import recipe_models


class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        recipe = recipe_models.Recipe.objects.create(
            name='Pizza',
            description='Put it in the oven',
            ingredients=[{"name": "dough"}, {"name": "cheese"}, {"name": "tomato"}]
        )
        self.assertEqual(str(recipe), recipe.name)
