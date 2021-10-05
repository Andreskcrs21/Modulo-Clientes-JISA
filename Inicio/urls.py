from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path("", views.inicio, name='inicio'),

    
]