#Django
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Models
from django.contrib.auth.models import User

# Utils
from datetime import timedelta


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, unique=True)
    body = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'

    def save(self, *args, **kwargs):
        user = self.user
        last_creation = user.recipe_set.all().last().created
        if last_creation < timezone.now()-timedelta(minutes=5):
             super(Recipe, self).save(*args, **kwargs)
        else:
            raise ValidationError(_('You can create a recipe every 5 minutes!'))

    @property
    def count_votes(self):
        return self.reciperanking_set.all().count()

<<<<<<< HEAD
    @property
    def sum_votes(self):
        ranking = self.reciperanking_set.all()
        ranks = [r.rank for r in ranking]
        return sum(ranks)
    
    @property
    def sum_votes_last_5_min(self):
        five_min_ago = timezone.now() - timedelta(minutes=5)
        ranking = self.reciperanking_set.filter(created__gte=five_min_ago)
        ranks = [r.rank for r in ranking]
        return sum(ranks)

    @property
    def sum_votes_last_hour(self):
        hour_ago = timezone.now() - timedelta(hours=1)
        ranking = self.reciperanking_set.filter(created__gte=hour_ago)
        ranks = [r.rank for r in ranking]
        return sum(ranks)

    @property
    def sum_votes_last_day(self):
        day_ago = timezone.now() - timedelta(days=1)
        ranking = self.reciperanking_set.filter(created__gte=day_ago)
        ranks = [r.rank for r in ranking]
        return sum(ranks)
=======
    def save(self, *args, **kwargs):
        user = self.user
        last_creation = user.recipe_set.all().last().created
        if last_creation < timezone.now()-timedelta(minutes=5):
             super(Recipe, self).save(*args, **kwargs)
        else:
            raise ValidationError(_('You can create a recipe every 5 minutes!'))
>>>>>>> 54d606264a3bf4b31937f94189cfbcc1111841ac


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

    def save(self, *args, **kwargs):
        user = self.user
        recipe = self.recipe
        last_creation = recipe.reciperanking_set.all().last().created
        # If in the last 2 min, we havent't created a recipe
        if last_creation < timezone.now()-timedelta(minutes=2):
             super(RecipeRanking, self).save(*args, **kwargs)
        else:
            raise ValidationError(_('You can vote a recipe every 2 minutes!'))
