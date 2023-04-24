"""sezane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import index, listar_prendas, guardar, agregar, editar_prenda, actualizar_prenda, eliminar_prenda,  buscar, TipoPrendas



urlpatterns = [
    
    path('', index, name='index'),
    path('prendas/', listar_prendas, name='prendas'),
    path('agregar/', agregar, name='agregar'),
    path('guardar/', guardar, name="guardar"),
    path('editar/<int:id_prenda>', editar_prenda, name="editar"),
    path('actualizar/<int:id_prenda>', actualizar_prenda, name="actualizar"),
    path('eliminar/<int:id_prenda>', eliminar_prenda, name="eliminar"),
    path('buscar/', buscar, name='buscar'),

    #prendas
    path('tangas/', TipoPrendas.tanga, name='tangas'),
    path('cacheteros/', TipoPrendas.cachetero, name='cacheteros'),
    path('topsDeportivos/', TipoPrendas.topDeportivo, name='topsDeportivos'),
    path('topsClasicos/', TipoPrendas.topClasico, name='topsClasicos'),
    path('shorts/', TipoPrendas.short, name='shorts'),
    path('duosClasicos/', TipoPrendas.duoClasico, name='duosClasicos'),
    path('duosDeportivos/', TipoPrendas.duoDeportivo, name='duosDeportivos'),
    path('duosShort/', TipoPrendas.duoShort, name='duosShort'),
    path('trios/', TipoPrendas.trio, name='trios'),
    path('boxers/', TipoPrendas.boxer, name='boxers'),



]
