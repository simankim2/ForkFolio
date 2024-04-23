from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe, Profile, Ingredient, Step, Rating
from recipes.forms import RecipeForm, ProfileForm, IngredientForm, StepForm, SignUpForm, IngredientFormSet, StepFormSet, RatingForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.db.models import Avg


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                user=request.user,
                recipe=recipe,
                defaults={'stars': form.cleaned_data['stars']}
            )
        return redirect('show_recipe', id=recipe.id)
    else:
        form = RatingForm()

    average_rating_result = recipe.ratings.aggregate(average=Avg('stars'))
    average_rating = average_rating_result['average'] if average_rating_result['average'] is not None else "No ratings yet"

    context = {
        "recipe_object": recipe,
        "rating_form": form,
        "average_rating": average_rating if average_rating is not None else "No ratings yet",
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.annotate(avg_rating=Avg('ratings__stars'))
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)


@login_required
def create_recipe(request):
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=3, can_delete=True)
    StepFormSet = inlineformset_factory(Recipe, Step, form=StepForm, extra=3, can_delete=True)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
            step_formset = StepFormSet(request.POST, instance=recipe)

            if ingredient_formset.is_valid() and step_formset.is_valid():
                ingredient_formset.save()
                step_formset.save()
                return redirect("recipe_list")  # Redirect after post

        else:
            ingredient_formset = IngredientFormSet(request.POST)
            step_formset = StepFormSet(request.POST)
    else:
        form = RecipeForm()
        ingredient_formset = IngredientFormSet()
        step_formset = StepFormSet()

    return render(request, 'recipes/create.html', {
        "form": form,
        "ingredient_formset": ingredient_formset,
        "step_formset": step_formset
    })


@login_required
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
        step_formset = StepFormSet(request.POST, instance=recipe)
        if form.is_valid() and ingredient_formset.is_valid() and step_formset.is_valid():
            form.save()
            ingredient_formset.save()
            step_formset.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=recipe)
        ingredient_formset = IngredientFormSet(instance=recipe)
        step_formset = StepFormSet(instance=recipe)

    context = {
        "recipe_object": recipe,
        "form": form,
        "ingredient_formset": ingredient_formset,
        "step_formset": step_formset,
    }
    return render(request, "recipes/edit.html", context)


@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, user=request.user)  # Ensure that recipe belongs to the user
    if request.method == 'POST':
        recipe.delete()
        return redirect('user_profile', username=request.user.username)  # Redirect to the profile page or wherever appropriate
    return redirect('show_recipe', id=id)  # If not POST, redirect back to the recipe detail page


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
    if request.user != request.user.profile.user:
        return HttpResponseForbidden("You are not allowed to edit this profile!")

    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'recipes/profile_edit.html', {'form': form})
