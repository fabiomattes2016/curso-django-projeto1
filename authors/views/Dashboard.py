from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from recipes.models import Recipe


@login_required(login_url='author-login', redirect_field_name='next')
def user_dashboard(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.filter(is_published=False, author=request.user)

    return render(request, 'authors/pages/dashboard_view.html', context={
        'recipes': recipes,
    })


@login_required(login_url='author-login', redirect_field_name='next')
def delete_recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe = Recipe.objects.filter(is_published=False, author=request.user, pk=recipe_id).first()

    if not request.POST:
        return render(request, 'authors/pages/404_error.html', status=404)

    if not recipe:
        return render(request, 'authors/pages/404_error.html', status=404)

    recipe.delete()

    messages.success(request, 'Receita excluida com sucesso!')

    url_redirect = reverse('author-dashboard')
    return HttpResponseRedirect(url_redirect)
