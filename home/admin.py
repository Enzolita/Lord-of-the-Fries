from django.contrib import admin
from .models import Recipe, Post, Ingredient, Author

# Register your models here.
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Author)
admin.site.register(Ingredient)