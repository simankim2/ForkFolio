from django.forms import ModelForm
from recipes.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]


class Edit_RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]
