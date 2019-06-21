from django.http import HttpResponse
from django.template import loader


from .models import Ingredient, Recipe

def index(request):
    template = loader.get_template('recipes2/index.html')

    recipes = Recipe.objects.all()  # or simply .values() to get all fields
    recipes = list(recipes)  # important: convert the QuerySet to a list object
    for recipe in recipes:
        recipe.ing = ','.join(list(map(lambda x : x.name, list(recipe.ingredients.all()))))
        print(recipe.ing)
    context = {
        'recipes': recipes
    }
    return HttpResponse(template.render(context, request))
