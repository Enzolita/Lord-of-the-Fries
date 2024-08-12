from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Recipe(models.Model):
    STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Published"),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    description = models.TextField()  # Short description of the recipe
    ingredients = models.TextField()  # List of ingredients
    instructions = models.TextField()  # Step-by-step cooking instructions
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    total_time = models.PositiveIntegerField(help_text="Total time in minutes", blank=True, null=True)
    servings = models.PositiveIntegerField(help_text="Number of servings")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.total_time:
            self.total_time = self.prep_time + self.cook_time
        super().save(*args, **kwargs)


        