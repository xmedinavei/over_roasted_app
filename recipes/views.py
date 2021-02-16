#Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy

#Forms
from recipes.forms import RecipeForm

#Models
from recipes.models import Recipe, RecipeRanking


class RecipeFeedView(LoginRequiredMixin, ListView):
    template_name = 'recipes/feed.html'
    model = Recipe
    ordering = ('?',)
    # paginate_by = 30
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.order_by('?')


class CreateRecipeView(LoginRequiredMixin, CreateView):
    template_name = 'recipes/new.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context