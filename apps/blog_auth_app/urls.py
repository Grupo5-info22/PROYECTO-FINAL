# Tipo el ÍNDICE
"""proyectofinalINFO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import SignUpView

app_name= 'apps.blog_auth_app'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('register', SignUpView.as_view(),name='register'),
    path('registercomplete', TemplateView.as_view(template_name='registration/registercomplete.html'),name='registercomplete'),
    path('welcome', TemplateView.as_view(template_name='registration/welcome.html'),name='welcomeview'),
]