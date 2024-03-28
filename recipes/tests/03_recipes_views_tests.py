from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes-home'))
        self.assertIs(view.func, views.home)

    def test_recipe_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes-details', kwargs={'recipe_id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_search_view_function_is_correct(self):
        view = resolve(reverse('recipes-search'))
        self.assertIs(view.func, views.search)
