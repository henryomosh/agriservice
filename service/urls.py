from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('about_us/', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', views.ContactTemplateView.as_view(), name='signup'),
    path('signup/', views.signup, name='account'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('account/', views.AccountTemplateView.as_view(), name='contact'),
]