from django.shortcuts import render

from recipe_app.forms.recipe import RecipeForm
from recipe_app.models import Recipe


def index(request):
    if Recipe.objects.exists():
        recipe = Recipe.objects.all()
        context = {
            'recipe': recipe,
        }
        return render(request, 'index.html', context)
    else:
        recipe = Recipe.objects.all()
        context = {
            'recipe': recipe,
        }
        return render(request, 'index.html', context)


"""

"""
