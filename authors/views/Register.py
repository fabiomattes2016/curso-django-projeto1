from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from authors.forms import RegisterForm


def register_view(request: HttpRequest) -> HttpResponse:
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
        'form_action': reverse('author-register-create'),
    })


def register_create(request: HttpRequest) -> HttpResponse:
    if not request.POST:
        return render(request, 'authors/pages/404_error.html', status=404)

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)

    if form.is_valid():
        account = form.save(commit=False)
        account.set_password(account.password)
        account.save()

        messages.success(request, 'Conta criada com sucesso! Efetue o login!')

        del (request.session['register_form_data'])

    url_redirect = reverse('author-login')
    return HttpResponseRedirect(url_redirect)
