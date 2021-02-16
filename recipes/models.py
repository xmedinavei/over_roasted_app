#Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    
    ranking = models.ManyToManyField('recipes.RecipeRanking', related_name='ranking_recipe', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'

    @property
    def count_votes(self):
        return self.ranking.all().count()


class RecipeRanking(models.Model):
    SUPER_BAD = '-5'
    BAD = '-2'
    NOT_OK = '-1'
    OK = '+1'
    GOOD = '+2'
    SUPER_GOOD = '+5'
    RANKING_CHOICES = [
        (SUPER_BAD, -5),
        (BAD, -2),
        (NOT_OK, -1),
        (OK, 1),
        (GOOD, 2),
        (SUPER_GOOD, 5),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    rank = models.FloatField(max_length=2, choices=RANKING_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Recipe: {self.recipe.title} Rank: {self.rank}'
