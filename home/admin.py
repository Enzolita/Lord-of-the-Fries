from django.contrib import admin
from .models import Author, Recipe, Ingredient, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Ingredient)