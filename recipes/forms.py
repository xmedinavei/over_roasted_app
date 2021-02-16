#Django
from django import forms

#Models
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('user', 'title', 'body')