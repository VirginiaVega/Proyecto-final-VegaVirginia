from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserEditForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
# def home(req):
#     return render(req, 'appv/index.html')

def about(req):
    return render(req, 'appv/acercade.html')

# def register(request):
#     if request.method == 'POST':
#             form = UserRegisterForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 form.save()
#                 return render(request,"appv/index.html" , {"mensaje":"Usuario Creado :)"})
#     else:  
#             form = UserRegisterForm()    
#     return render(request,"appv/registro.html" ,  {"form":form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            is_superuser = form.cleaned_data['is_superuser']
            
            # Crear el usuario
            user = form.save(commit=False)
            user.is_superuser = is_superuser
            user.is_staff = is_superuser  # El superusuario también debe ser 'staff'
            user.save()

            # Redirigir a una página de éxito
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, "appv/registro.html", {"form": form})








@login_required
def editar_perfil(request):
    usuario = request.user 
    if request.method == 'POST': 
        miFormulario = UserEditForm(request.POST, instance=usuario) 
        if miFormulario.is_valid(): 
            miFormulario.save() 
            logout(request)
            return redirect('login')
    else: 
        miFormulario = UserEditForm(instance=usuario)
    
    return render(request, "appv/editarPerfil.html", {"mi_form": miFormulario, "usuario": usuario})
