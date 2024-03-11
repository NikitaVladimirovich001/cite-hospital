from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auth_.forms import AuthForm, RegForm


def login(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())

            return HttpResponseRedirect(reverse('glav'))
    else:
        form = AuthForm()
    context = {'form': form}

    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegForm(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('glav'))
    else:
        form = RegForm()
    context = {'form': form}

    return render(request, 'register.html', context)
