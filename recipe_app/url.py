from django.urls import path

from recipe_app.vies.index import index
from recipe_app.vies.recipe import create_recipe, edit_recipe, delete_recipe, recipe_details

"""
•	'/' - home page
•	'/create' - create recipe page
•	'/edit/:id' - edit recipe page
•	'/delete/:id' - delete recipe page
•	'/details/:id' - recipe details page

"""
urlpatterns = [
    path('', index, name='index'),

    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', recipe_details, name='recipe details'),
]
