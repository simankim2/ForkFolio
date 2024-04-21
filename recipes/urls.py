from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe


urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("signup/", signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="recipes/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="recipe_list"), name='logout'),
]
