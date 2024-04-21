from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from recipes.forms import SignUpForm


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)

@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }

    return render(request, "recipes/create.html", context)

@login_required
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=recipe)

    context = {
        "recipe_object": recipe,
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("recipe_list")
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, "recipes/signup.html", context)
