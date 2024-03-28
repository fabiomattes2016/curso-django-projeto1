from django.urls import path
from recipes.views import Home, Recipe, Category, Search


urlpatterns = [
    path('', Home.home, name="recipes-home"),
    path('recipes/search/', Search.search, name="recipes-search"),
    path('recipes/category/<int:category_id>/', Category.category, name="category"),
    path('recipes/<int:recipe_id>/', Recipe.recipe, name="recipes-details"),
]
