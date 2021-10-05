from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistroForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Autos.models import Auto, Moto

def inicio(request):
    return render(request, "login/inicio.html", {"autos":Auto.objects.all , "motos":Moto.objects.all})
