#  Models
from django.contrib.auth.models import User
from recipes.models import Recipe, RecipeRanking

# Utils
from statistics import mean

# Top 10 voted, clicks
# def top_10_voted():
#     top_10_voted = Recipe.objects.annotate(
#         ranking_count=Count('reciperanking')
#     )[:10][::-1]
#     return top_10_voted


# Top scores #

def top_10():
    top_10_dict = {}
    for r in Recipe.objects.all():
        top_10_dict[r] = r.sum_votes
        top_10_dict_sorted = sorted(top_10_dict.items(), key=lambda x: x[1], reverse=True)
        top_10 = [r[0] for r in top_10_dict_sorted][:10]
    return top_10


def top_10_last_5_min():
    last_5_min_votes = {}
    for r in Recipe.objects.all():
        last_5_min_votes[r] = r.sum_votes_last_5_min
        last_5_sorted = sorted(last_5_min_votes.items(), key=lambda x: x[1], reverse=True)
        top_10_last_5_min = [r[0] for r in last_5_sorted][:10]
        return top_10_last_5_min


def top_10_last_hour():
    last_hour_votes = {}
    for r in Recipe.objects.all():
        last_hour_votes[r] = r.sum_votes_last_hour
        last_hour_sorted = sorted(last_hour_votes.items(), key=lambda x: x[1], reverse=True)
        top_10_last_hour = [r[0] for r in last_hour_sorted][:10]
    return top_10_last_hour


def top_10_last_day():
    last_day_votes = {}
    for r in Recipe.objects.all():
        last_day_votes[r] = r.sum_votes_last_day
        last_day_sorted = sorted(last_day_votes.items(), key=lambda x: x[1], reverse=True)
        top_10_last_day = [r[0] for r in last_day_sorted][:10]
    return top_10_last_day


# Comensales

def comensal_exigente_score(u):
    from statistics import mean
    votes = RecipeRanking.objects.filter(user=u)
    if votes:
        votes_list = [v.rank for v in votes]
        max_vote = max([v.rank for v in votes])
        mean_vote = mean(votes_list)
        num_votes = len(votes_list)

        votes_dict = {}
        for v in votes:
            votes_dict[v] = v.rank
            votes_dict_sorted = sorted(votes_dict.items(), key=lambda x: x[1], reverse=True)

        r_most_voted = next(iter(votes_dict_sorted))[0] 
        recipe_count = RecipeRanking.objects.filter(user=u,recipe=r_most_voted.recipe).count()

        comensal_exigente_score = (max_vote - mean_vote) * (num_votes - recipe_count)
        return comensal_exigente_score
    else: 
        return 0