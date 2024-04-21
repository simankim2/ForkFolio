from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import Recipe, Profile


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]


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
