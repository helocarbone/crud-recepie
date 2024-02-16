from rest_framework import serializers

from core.recipe_models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['ingredients', 'description']

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)
