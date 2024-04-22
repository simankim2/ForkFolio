from django.forms import ModelForm, inlineformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import Recipe, Profile, Ingredient, Step


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "item",
        ]


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ["step_text"]


IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient,
    form=IngredientForm,
    extra=3,  # Specifies the number of empty forms the formset should display
    can_delete=True  # Adds a boolean field on each form to mark an instance for deletion
)

StepFormSet = inlineformset_factory(
    Recipe, Step,
    form=StepForm,
    extra=3,
    can_delete=True
)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'email', 'about_me']
