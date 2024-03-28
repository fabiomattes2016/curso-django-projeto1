from django.urls import path
from authors.views import Register, Login, Dashboard, DashboardRecipeEdit, DashboardRecipeCreate


urlpatterns = [
    path('register/', Register.register_view, name="author-register"),
    path('register/create', Register.register_create, name="author-register-create"),
    path('login/', Login.login_view, name="author-login"),
    path('login/create', Login.login_create, name="author-login-create"),
    path('logout/', Login.user_logout, name="author-logout"),
    path('dashboard/', Dashboard.user_dashboard, name="author-dashboard"),
    path('dashboard/recipe/create/',
         DashboardRecipeCreate.dashboard_recipe_create,
         name="dashboard-recipe-create"),
    path('dashboard/recipe/<int:recipe_id>/edit/',
         DashboardRecipeEdit.dashboard_recipe_edit,
         name="dashboard-recipe-edit"),
    path('dashboard/recipe/<int:recipe_id>/delete/',
         Dashboard.delete_recipe,
         name="dashboard-recipe-delete"),
    # path('recipes/search/', views.search, name="recipes-search"),
    # path('recipes/category/<int:category_id>/', views.category, name="category"),
    # path('recipes/<int:recipe_id>/', views.recipe, name="recipes-details"),
]
