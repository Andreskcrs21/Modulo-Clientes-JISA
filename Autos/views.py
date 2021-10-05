from django.core import paginator
from django.core.checks import messages
from django.http.response import Http404
from django.shortcuts import render, redirect
from .forms import AutosForm, MotoForm
from Autos.models import*
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def lista_autos(request):
    busqueda = request.GET.get("buscar")
    autos = Auto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(autos, 3)
        autos = paginator.page(page)

    except:
        raise Http404

    if busqueda:
        autos = Auto.objects.filter(
            Q(Marca__icontains = busqueda) | 
            Q(Modelo__icontains = busqueda)
        ).distinct()
    return render(request, 'carros/lista_autos.html', {"entity":autos, "paginator" : paginator})            

# View Motos

def lista_moto(request):
    busqueda = request.GET.get("buscar")
    motos = Moto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(motos, 3)
        motos = paginator.page(page)

    except:
        raise Http404

    if busqueda:
        motos = Moto.objects.filter(
            Q(Marca__icontains = busqueda) | 
            Q(Modelo__icontains = busqueda)
        ).distinct()
    return render(request, 'carros/lista_motos.html', {"entity":motos, "paginator": paginator})
  
def detalle_moto(request, id):
    motos = Moto.objects.filter(id = id)
    return render(request, 'carros/detalle_motos.html', {"motos":motos})

def detalle_auto(request, id):
    autos = Auto.objects.filter(id = id)
    return render(request, 'carros/detalle_auto.html', {"autos":autos})

def busquedaAuto(request):
    busqueda = request.GET.get("buscar")
    autos = Auto.objects.all()
    if busqueda:
        autos = Auto.objects.filter(
            Q(Marca__icontains = busqueda) | 
            Q(Modelo__icontains = busqueda)
        ).distinct()
    return render(request, 'carros/lista_autos.html', {'autos' : autos})