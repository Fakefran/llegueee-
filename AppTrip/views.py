from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from AppTrip.forms import *




#Vista de inicio:
def inicio(request):
    return render(request,"AppTrip/inicio.html")





#Vista de login:

def iniciarSesion(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario = info["username"]
            contra = info["password"]
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                
                login(request,user)
                
                return render(request, "AppTrip/iniciobienvenida.html", {"mensaje": f"Bienvenido{user}"})
            
            
        else:
            return render(request, "AppTrip/iniciobienvenida.html", {"mensaje":"Los datos son incorrectos"})
        
    else:
        
        form = AuthenticationForm()
        
        
    return render(request, "AppTrip/registro/login.html",{"formulario":form})




#Vista para registrarse:

def Registro(request):
    if request.method == "POST":
    
    
     form = UsuarioRegistro(request.POST)
     
     if form.is_valid():
         
        info= form.cleaned_data
         
        usuario = info['first_name']
         
         
        form.save()
        
         
        return render(request, "AppTrip/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
    
    else:
        form = UsuarioRegistro()  
      
    return render(request, "AppTrip/registro/registro.html",{"formulario":form})



#Vista cerrar sesion:

def CerrarSesion(request):
    logout(request)
    
    return render(request, "AppTrip/registro/logout.html")



@login_required
def EditUsuario(request):
    usuario= request.user 
    if request.method == "POST":
    
        form = formularioEditar(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
        
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            
            usuario.save()
            
            return render(request,"AppTrip/inicio.html")

    else:
        form = formularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            })
        
        
    return render(request,"AppTrip/registro/editarperfil.html",{"formulario": form, "usuario":usuario} )

#Vista agregar avatar:

@login_required
def AgregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"] )
            avatar.save()
            return render(request, "AppTrip/inicio.html")


    else:
        
        form = AvatarFormulario()
    
    return render(request, "AppTrip/agregaravatar.html", {"formulario":form})




#Vista lugar:
def lugarFormulario(request):
    return render(request, "AppTrip/lugares/lugares.html")
class Listalugar(ListView):
      model= lugar
      template_name="AppTrip/lugares/lugares_list.html"
class Detallelugar(DetailView):
      model = lugar
      template_name="AppTrip/lugares/lugares_detail.html"
      context_object_name = "lugar"
class Crearlugar(CreateView):
    model=lugar
    success_url = reverse_lazy('lugarLista')
    fields = ["destino", "tipodeclima","reseña",]
    template_name="AppTrip/lugares/lugares_form.html"

class Actualizarlugar(UpdateView):
    model = lugar
    success_url = reverse_lazy('lugarLista')
    fields = ["destino", "tipodeclima","reseña",]
    template_name="AppTrip/lugares/lugares_form.html"
class Borrarlugar(DeleteView):
    model = lugar
    success_url = reverse_lazy('lugarLista')
    template_name="AppTrip/lugares/lugares_confirm_delete.html"
    
    
#Buscar Lugares:
def lista_lugares(request):
    form = BuscarLugarForm(request.GET)
    lugares = lugar.objects.all()

    if form.is_valid():
        busqueda = form.cleaned_data['busqueda']
        lugares = lugares.filter(destino__icontains=busqueda)

    return render(request, 'lista_lugares.html', {'form': form, 'lugares': lugares})
  
  #Vista agenciaDeviajess:


#Vista Agencia De viajess:
def agenciaDeviajesFormulario(request):
    return render(request, "AppTrip/agenciadeviajess/agenciaDeviajes.html")
class ListaagenciaDeviajes(ListView):
    model= agenciaDeviajes
    template_name="AppTrip/agenciadeviajes/agenciadeviajes_list.html"
class DetalleagenciaDeviajes(DetailView):
      model = agenciaDeviajes
      template_name="AppTrip/agenciadeviajes/agenciadeviajes_detail.html"
class CrearagenciaDeviajes(CreateView):
    model = agenciaDeviajes
    success_url = reverse_lazy('agenciaDeviajesLista')
    fields = ["nombre","telefono","email","reseña",]
    template_name="AppTrip/agenciadeviajes/agenciadeviajes_form.html"
class ActualizaragenciaDeviajes(UpdateView):
    model = agenciaDeviajes
    success_url = reverse_lazy('agenciaDeviajesLista')
    fields = ["nombre", "telefono","email","reseña",]
    template_name="AppTrip/agenciadeviajes/agenciadeviajes_form.html"
class BorraragenciaDeviajes(DeleteView):
    model = agenciaDeviajes
    success_url = reverse_lazy('agenciaDeviajesLista')
    template_name = "AppTrip/agenciadeviajes/agenciadeviajes_confirm_delete.html"
    
  
    

    #Vista Obra Social:





#Vista Hotelesl:
def hotelFormulario(request):
    return render(request, "AppTrip/hotel.html")
class Listahotel(ListView):
      model= hotel
      template_name="AppTrip/hoteles/hoteles_list.html"  
class Detallehotel(DetailView):
      model = hotel
      template_name="AppTrip/Hoteles/hoteles_detail.html"    
class Crearhotel(CreateView):
    model = hotel
    success_url = reverse_lazy('hotelLista')
    fields = ["nombre", "ciudad", "calle","numero","email","telefono","reseña",]
    template_name="AppTrip/Hoteles/hoteles_form.html"
class Actualizarhotel(UpdateView):
    model = hotel
    success_url = reverse_lazy('hotelLista')
    fields = ["nombre", "ciudad", "calle","numero","email","telefono","reseña",]
    template_name="AppTrip/Hoteles/hoteles_form.html"
class Borrarhotel(DeleteView):
    model = hotel
    success_url = reverse_lazy('hotelLista')
    template_name="AppTrip/Hoteles/hoteles_confirm_delete.html"






    
    