from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404

from .models import Ingredient


def get_all_ingredients(request):
    ingredients = Ingredient.objects.all().values('id', 'name')  # or simply .values() to get all fields
    ingredients = list(ingredients)  # important: convert the QuerySet to a list object
    return JsonResponse(ingredients, safe=False)

def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    ingredient.delete()
    return HttpResponse(status=201)

def add_ingredient(request, ingredient_name):
    ingredient = Ingredient(name=ingredient_name)
    ingredient.save()
    data = serializers.serialize('json', [ingredient])
    return HttpResponse(data, content_type="application/json")
