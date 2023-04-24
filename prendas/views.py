from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.db.models import Q 
# from .forms import Formularios
from prendas.models import Prendas
from .forms import Buscar
from prendas.forms import Formulario

# Create your views here.


def index(request):

    return render(request, 'index.html')



def buscar(request):

    
    query = request.GET.get('query')
    opcion = request.GET.get('opcion')

    if opcion == 'Prenda':
        results = Prendas.objects.filter(prenda__icontains=query).distinct()
    elif opcion == 'Talla':
        results = Prendas.objects.filter(talla__icontains=query).distinct()
    elif opcion == 'Color':
        results = Prendas.objects.filter(color__icontains=query).distinct()
    elif opcion == 'Cantidad':
        results = Prendas.objects.filter(cantidad__icontains=query).distinct()

    context = {'prendas': results}
    return render(request, 'busqueda.html', context)



def agregar(request):
    prenda = Formulario()
    return render(request, 'agregar.html', {'form':prenda})



def guardar(request):

        prenda = Formulario(request.POST)

        if prenda.is_valid():
            prenda.save()
            prenda = Formulario()
            

        else:
            prenda = Formulario()


        return render(request, 'agregar.html', {'form':prenda, 'msgOK':'OK'})


def listar_prendas(request):
        prendas = Prendas.objects.all()
        query = request.GET.get('query')
        opcion = request.GET.get('opcion')
        if query and opcion:

         if opcion == 'Prenda':
            results = Prendas.objects.filter(prenda__icontains=query)
        elif opcion == 'Talla':
            results = Prendas.objects.filter(talla__icontains=query)
        elif opcion == 'Color':
            results = Prendas.objects.filter(color__icontains=query)
        elif opcion == 'Cantidad':
            results = Prendas.objects.filter(cantidad__icontains=query)

            context = {'results': results}
            return render(request, 'prendas.html', context)
        return render(request, 'prendas.html', {"prendas":prendas})



def editar_prenda(request, id_prenda):

        prenda = Prendas.objects.filter(id=id_prenda).first() #filter para que me filtre por id y first para que me traiga el primer dato
        form = Formulario(instance=prenda)
        return render(request, 'editar.html', {"form":form, "prenda":prenda})



def actualizar_prenda(request, id_prenda):

        prenda = Prendas.objects.get(pk=id_prenda) #(pk=primary key)  get para seleccionar el objeto en la base de datos
        form = Formulario(request.POST, instance=prenda) #con request post le digo que obtenga los datos que se ingresaron en el formulario
        # y lo matchee con el objeto de la base de datos

        if form.is_valid(): #si el formulario es valido
            form.save()

        prendas = Prendas.objects.all() #hacemos de nuevo una peticion a la base de datos para redireccionar al usuario a la lista de familiares despues de actualizar el objeto
        return render(request, 'prendas.html', {"prendas":prendas})


def eliminar_prenda(request, id_prenda):

        prenda = Prendas.objects.get(pk=id_prenda) #seleccionamos el objeto de la base de datos que queremos eliminar, buscamos el id
        prenda.delete() #metodo delete 
        prendas = Prendas.objects.all()
        return render(request, 'prendas.html', {"prendas":prendas, "msg":"OK"})#agregamos la variable msg para habilitar la alerta del mensaje cuando el alumno sea eliminado correctamente
        


class TipoPrendas:
     
    def tanga(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Tanga').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def cachetero(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Cachetero').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def topClasico(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Top Clasico').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def topDeportivo(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Top Deportivo').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def short(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Short').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def duoClasico(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Duo Clasico').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def duoDeportivo(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Duo Deportivo').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def duoShort(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Duo Short').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def trio(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Trio').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})
    
    def boxer(request):
         
        prenda = Prendas.objects.filter(prenda__icontains='Boxer').distinct()
        return render(request, 'prendas.html', {'prendas':prenda})