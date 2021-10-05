from django.urls import path, include
from . import views

urlpatterns = [
    path('lista_autos/', views.lista_autos, name="lista_autos"),
    path('lista_motos/', views.lista_moto, name="lista_motos"),
    path('detalle_moto/<int:id>/', views.detalle_moto, name="detalle_moto"),
    path('detalle_auto/<int:id>/', views.detalle_auto, name="detalle_auto"),
    path('buscar_auto/', views.busquedaAuto, name="buscar_auto")
]