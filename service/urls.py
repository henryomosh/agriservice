from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    path('about_us/', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('account/', views.AccountTemplateView.as_view(), name='account'),
]