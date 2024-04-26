from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import signup
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe, delete_recipe, profile_view, profile_edit


urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("recipe/delete/<int:id>/", delete_recipe, name="delete_recipe"),
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="recipes/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="recipe_list"), name="logout"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("profile/", profile_view, name="my_profile", kwargs={"username": None}),
    path("profile/<str:username>/", profile_view, name="user_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
