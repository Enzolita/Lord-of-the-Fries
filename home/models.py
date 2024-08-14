from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    TAGS = [
        ('LACTOSEFREE', 'Lactose-free'),
        ('VEGAN', 'Vegan'),
        ('GLUTEN_FREE', 'Gluten-Free'),
        ('KETO', 'Keto'),
        ]

    STATUS = [
        ("unpublished", "Unpublished"),
    ]
    """
    Represents a recipe with ingredients, an image, and related comments.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=100, choices=TAGS, default="recipe")
    featured_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    estimated_time = models.IntegerField("Estimated time")
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default="unpublished")
    likes = models.ManyToManyField(User, related_name="recipe_like", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        ingredients_list = [
            f"{ingredient.amount} {ingredient.unit} {ingredient.ingredient}"
            for ingredient in self.ingredient_set.all()
        ]
        return f"{self.title} - {' | '.join(ingredients_list)}"

    def number_of_likes(self):
        """
        Return the count of likes for this recipe.
        """
        return self.likes.count()


class Ingredient(models.Model):
    """
    Represents an ingredient which is associated with a specific recipe.
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.ingredient


class Author(models.Model):
    STATUS_CHOICES = (
        (0, "Inactive"),
        (1, "Active"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="author_profile"
    )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)  # Short biography of the author
    profile_picture = models.ImageField(
        upload_to="author_pictures/", blank=True, null=True
    )  # Profile picture
    website = models.URLField(blank=True, null=True)  # Personal or professional website
    social_links = models.JSONField(
        blank=True, null=True, help_text="Social media links in JSON format"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    STATUS_CHOICES = (
        (0, "Pending"),
        (1, "Approved"),
        (2, "Rejected"),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="comments",
        blank=True,
        null=True,
    )
    content = models.TextField()  # The content of the comment
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_on.strftime('%Y-%m-%d %H:%M')}"
