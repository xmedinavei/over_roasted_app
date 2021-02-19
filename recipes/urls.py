# Django
from django.urls import path

# Views
from recipes import views

urlpatterns = [
    path(
        route='',
        view=views.RecipeFeedView.as_view(),
        name='feed'
    ),
    path(
        route='new/',
        view=views.CreateRecipeView.as_view(),
        name='create'
    ),
    path(
        route='vote/',
        view=views.vote_view,
        name='vote'
    ),
    path(
        route='results/',
        view=views.results_view,
<<<<<<< HEAD
        name='results'
=======
        name='resuts'
>>>>>>> 54d606264a3bf4b31937f94189cfbcc1111841ac
    )
]