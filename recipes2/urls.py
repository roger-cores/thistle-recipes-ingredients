from django.urls import path

from . import views
from . import apis

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:recipe>/ingredient/<str:ingredient>', apis.add_or_remove_ingredient, name='add_ingredient_to_recipe'),
    path('<str:recipe>/ingredient/<str:ingredient>', apis.add_or_remove_ingredient, name='remove_ingredient_to_recipe'),
]
