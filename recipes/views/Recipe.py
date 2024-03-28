import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from recipes.models import Recipe


PER_PAGE = int(os.environ.get('PER_PAGE', 9))


def recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe_selected = Recipe.objects.filter(pk=recipe_id).first()

    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': recipe_selected,
        'is_detail': True
    })
