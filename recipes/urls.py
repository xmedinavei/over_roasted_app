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
    # path(
    #     route='<int:pk>/',
    #     view=views.RecipeVoteView.as_view(),
    #     name='vote'
    # )
]