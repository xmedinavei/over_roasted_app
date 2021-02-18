#Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count

#Forms
from recipes.forms import RecipeForm

#Models
from recipes.models import Recipe, RecipeRanking
from django.contrib.auth.models import User


class RecipeFeedView(LoginRequiredMixin, ListView):
    template_name = 'recipes/feed.html'
    model = Recipe
    ordering = ('?',)
    paginate_by = 1
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


def vote_view(request):
    if request.POST:
        recipe_id = request.POST['recipe_id']
        rate_tag = request.POST['rate']
        username = request.user.username
    
        recipe = Recipe.objects.get(id=recipe_id)
        user = User.objects.get(username=username)

        # import pdb; pdb.set_trace()
        RecipeRanking.objects.create(
            user=user,
            recipe=recipe,
            rank=rate_tag
        )
    return redirect(request.META.get('HTTP_REFERER'))

def results_view(self):
    if request.GET:
        top_recipes = Recipe.objects.annotate(
            ranking_count=Count('reciperanking')
        )[:10][::-1]
    pass

