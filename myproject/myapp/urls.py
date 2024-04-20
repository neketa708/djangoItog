from django.urls import path
from .views import home, recipe_detail, add_edit_recipe
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),
    path('add/', add_edit_recipe, name='add_recipe'),
    path('edit/<int:id>/', add_edit_recipe, name='edit_recipe'),
    path('login/', LoginView.as_view(), name='login'),
    # Другие маршруты на ваш выбор
]

