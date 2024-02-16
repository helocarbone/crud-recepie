from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.recipe_models import Recipe

from recipe.serializers import (
    RecipeSerializer,
    RecipeDetailSerializer,
)

RECIPE_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    return reverse('recipe:recipe-detail', args=[recipe_id])


def detail_url_query_params(recipe_name):
    return reverse('recipe:recipe-detail') + '?name=' + recipe_name


def create_recipe(**params):
    defaults = {
        'name': 'Test Recipe',
        'description': 'Description of recipe',
        'ingredients': [{'name': 'Ingredient1'}, {'name': 'Ingredient2'}]
    }

    defaults.update(params)
    recipe = Recipe.objects.create(**defaults)
    return recipe


class PublicRecipeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_recipes(self):
        create_recipe()
        create_recipe()
        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_recipe_by_id(self):
        recipe = create_recipe()

        url = detail_url(recipe.id)
        res = self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.data, serializer.data)
