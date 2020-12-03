from django.contrib import admin

# Register your models here.
from recipe_app.models import Recipe

admin.site.register(Recipe)