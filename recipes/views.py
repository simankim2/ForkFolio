from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe, Profile
from recipes.forms import RecipeForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect("profile_view", username=request.user.username)
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


@login_required
def profile_view(request, username=None):
    user = request.user if username is None else get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    recipes = Recipe.objects.filter(user=user)
    return render(request, 'recipes/profile.html', {'profile': profile, 'recipes': recipes})


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'recipes/profile_edit.html', {'form': form})
