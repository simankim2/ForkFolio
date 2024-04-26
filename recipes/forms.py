from django.forms import ModelForm, inlineformset_factory, ImageField, URLField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import Recipe, Profile, Ingredient, Step, Rating


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'review_text']


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
    profile_picture = forms.ImageField(required=False, help_text='Optional. Upload a profile picture.')
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "profile_picture"
        ]


class ProfileForm(ModelForm):
    profile_picture = ImageField(required=False)
    profile_picture_url = URLField(required=False, help_text='Optional. Provide a URL for your profile picture.')

    class Meta:
        model = Profile
        fields = ['name', 'location', 'email', 'about_me', 'profile_picture', 'profile_picture_url']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
