#Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count
from django.utils import timezone

#Forms
from recipes.forms import RecipeForm

#Models
from recipes.models import Recipe, RecipeRanking
from django.contrib.auth.models import User

# Utils
from datetime import timedelta
from recipes.utils import *
from statistics import mean


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


def results_view(request):
    '''
    functions:
    top_10(), top_10_last_5_min(), top_10_last_hour(), top_10_last_day(), comensal_exigente_score(u)
    are created in recipes/utils.py
    '''

    top10 = top_10() # Top 10 score
    top10_last_5_min = top_10_last_5_min()
    top10_last_hour = top_10_last_hour()
    top10_last_day = top_10_last_day()

    # Comensal mas exigente
    u_exigente_dict = {u:comensal_exigente_score(u) for u in User.objects.all()}
    u_exigente_dict_sorted = sorted(u_exigente_dict.items(), key=lambda x: x[1], reverse=True)
    u_exigente = next(iter(u_exigente_dict_sorted))[0]

    # Comensal menos exigente: El que menos ha votado
    u_votes_dict = {u:Recipe.objects.all().filter(user=u).count() for u in User.objects.all()}
    u_votes_dict_sorted = sorted(u_votes_dict.items(), key=lambda x: x[1])
    u_menos_exigente = next(iter(u_votes_dict_sorted))[0]

    # Render
    context = {}
    context['top10'] = top10
    context['top10_last_5_min'] = top10_last_5_min
    context['top10_last_hour'] = top10_last_hour
    context['top10_last_day'] = top10_last_day
    context['u_exigente'] = u_exigente
    context['u_menos_exigente'] = u_menos_exigente
    
    return render(request=request, template_name='recipes/results.html', context=context)








        


        
