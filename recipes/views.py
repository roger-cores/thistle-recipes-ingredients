from django.http import HttpResponse
from django.template import loader


from .models import Ingredient

def index(request):
    template = loader.get_template('recipes/index.html')

    ingredients = Ingredient.objects.all().values('name')  # or simply .values() to get all fields
    ingredients = list(ingredients)  # important: convert the QuerySet to a list object
    print(ingredients)
    context = {
        'tokens': ','.join(list(map(lambda x : x['name'], ingredients)))
    }
    return HttpResponse(template.render(context, request))
