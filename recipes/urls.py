from django.urls import path

from . import views
from . import apis

urlpatterns = [
    path('view', views.index, name='index'),
    path('get_all_ingredients', apis.get_all_ingredients, name='get_all_ingredients'),
    path('<str:ingredient_id>/delete', apis.delete_ingredient, name='delete_ingredient'),
    path('add/<str:ingredient_name>', apis.add_ingredient, name='add_ingredient')
]
