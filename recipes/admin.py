from django.contrib import admin
from .models import Recipe, Rating, Ingredient, Step, Profile


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'stars']
    list_filter = ['user', 'recipe']
    search_fields = ['user__username', 'recipe__title']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'amount', 'item']
    list_filter = ['recipe']
    search_fields = ['item']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'step_text']
    list_filter = ['recipe']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'location', 'email']
    search_fields = ['user__username', 'name', 'email']
