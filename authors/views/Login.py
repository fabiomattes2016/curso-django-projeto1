from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from authors.forms import LoginForm


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        url_redirect = reverse('author-dashboard')
        return HttpResponseRedirect(url_redirect)

    form = LoginForm()

    return render(request, 'authors/pages/login_view.html', context={
        'form': form,
        'form_action': reverse('author-login-create'),
    })


def login_create(request: HttpRequest) -> HttpResponse:
    if not request.POST:
        return render(request, 'authors/pages/404_error.html', status=404)

    POST = request.POST
    form = LoginForm(POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Usuário autenticado!')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Usuário e/ou Senha inválidos!')

    url_redirect = reverse('author-dashboard')
    return HttpResponseRedirect(url_redirect)


@login_required(login_url='author-login', redirect_field_name='next')
def user_logout(request: HttpRequest) -> HttpResponse:
    url_redirect = reverse('author-login')

    if not request.POST:
        return render(request, 'authors/pages/404_error.html', status=404)

    user_logged = request.user.username

    if request.POST.get('username') != user_logged:
        return render(request, 'authors/pages/404_error.html', status=404)

    logout(request)

    return HttpResponseRedirect(url_redirect)
