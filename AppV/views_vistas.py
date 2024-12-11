from django.views.generic import ListView
from .models import Entrada
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

def login_request(request):
    if request.method == "POST": 
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid(): 
            usuario = form.cleaned_data.get("username")  
            clave = form.cleaned_data.get("password") 
            nombre_usuario = authenticate(username=usuario, password=clave) 

            if nombre_usuario is not None:  
                login(request, nombre_usuario)
                return redirect('list')

            else: 
                return render(request, "appv/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  
        else: 
            return render(request, "appv/login.html", {"mensaje":"Datos incorrectos", "form": form})

    form = AuthenticationForm() 
    return render(request, "appv/login.html", {"form":form})



class EntradaCrear(CreateView):
    model = Entrada
    template_name = "appv/vistas_clases/nuevaEntrada.html" 
    success_url = reverse_lazy("list")
    fields= ["titulo", "subtitulo", "cuerpo", "autor", "imagen"]

class EntradasListView(LoginRequiredMixin, ListView):
    model = Entrada
    template_name = "appv/vistas_clases/listado.html" 

class EntradaDetalle(LoginRequiredMixin, DetailView):
    model = Entrada
    template_name = "appv/vistas_clases/detalleEntrada.html" 

class EntradaEditar(UpdateView):
    model = Entrada
    template_name = "appv/vistas_clases/editarEntrada.html" 
    success_url = reverse_lazy("list")
    fields= ["titulo", "subtitulo", "cuerpo", "autor", "imagen"]

class EntradaEliminar(DeleteView):
    model = Entrada
    success_url = reverse_lazy("list")
    template_name = "appv/vistas_clases/eliminarEntrada.html" 
