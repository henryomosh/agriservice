from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from .models import *


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class AccountTemplateView(TemplateView):
    template_name = 'account.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service:home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'home.html'







