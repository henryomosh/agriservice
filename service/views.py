from django.shortcuts import render
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class AccountTemplateView(TemplateView):
    template_name = 'account.html'

