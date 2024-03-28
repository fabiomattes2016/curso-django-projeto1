import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from recipes.models import Recipe
from utils.pagination import make_pagination


PER_PAGE = int(os.environ.get('PER_PAGE', 9))


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    pagination = make_pagination(request, recipes, PER_PAGE, 4)

    return render(request, 'global/pages/home.html', status=200, context={
        'recipes': pagination['page_object'],
        'is_detail': False,
        'pagination_range': pagination['pagination_range']
    })
