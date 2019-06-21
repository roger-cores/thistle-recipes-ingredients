from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Ingredient, Recipe

def add_or_remove_ingredient(request, recipe, ingredient):
    if request.method == 'DELETE':
        recipe = Recipe.objects.get(name=recipe)
        ingredient = Ingredient.objects.get(name=ingredient)
        recipe.ingredients.remove(ingredient)
    elif request.method == 'POST':
        recipe = Recipe.objects.get(name=recipe)
        try:
            ingredient = Ingredient.objects.get(name=ingredient)
        except:
            ingredient = Ingredient(name=ingredient)
            ingredient.save()
        recipe.ingredients.add(ingredient)
    return HttpResponse(status=201)
