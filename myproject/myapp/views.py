from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
# Create your views here.

def index(request):
    return HttpResponse("hhhhhh")


def home(request):
    # Получаем 5 случайных рецептов
    random_recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'home.html', {'recipes': random_recipes})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def add_edit_recipe(request, id=None):
    if id:
        recipe = Recipe.objects.get(id=id)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Сохраняем текущего пользователя как автора рецепта
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'add_edit_recipe.html', {'form': form, 'edit': id is not None})