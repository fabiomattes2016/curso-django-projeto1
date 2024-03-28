from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from recipes.models import Recipe
from authors.forms import AuthorRecipeForm


@login_required(login_url='author-login', redirect_field_name='next')
def dashboard_recipe_edit(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe = Recipe.objects.filter(pk=recipe_id, is_published=False, author=request.user).first()
    form = AuthorRecipeForm(data=request.POST or None, files=request.FILES or None, instance=recipe)

    if not recipe:
        return render(request, 'authors/pages/404_error.html', status=404)

    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_published = False
        recipe.save()

        messages.success(request, 'Receita salva com sucesso!')
        url_redirect = reverse('author-dashboard')

        return HttpResponseRedirect(url_redirect)

    return render(request, 'authors/pages/dashboard_recipe.html', context={
        'recipe': recipe,
        'form': form,
    })
