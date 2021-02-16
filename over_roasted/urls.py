
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include(('recipes.urls', 'recipes'), namespace='recipes')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]