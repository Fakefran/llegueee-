
from django.urls import path
from AppTrip.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
path('', inicio, name="inicio"),
path("login/", iniciarSesion, name="Login"),
path("registrarse/", Registro, name="registro"),
path("logout/", CerrarSesion, name="Logout"),
path("editar/", EditUsuario, name="Editarperfil" ),
path("avatar/", AgregarAvatar, name="cambiarAvatar"),



    
    #CRUD lugares :
path("lugares/lista/", Listalugar.as_view(), name="lugarLista"),
path("lugares/<int:pk>/", Detallelugar.as_view(), name="lugarDetalle"),  
path("lugares/crear/", Crearlugar.as_view(), name="lugarCrear"),
path("lugares/editar/<int:pk>/", Actualizarlugar.as_view(), name="lugarEditar"),
path("lugares/borrar/<int:pk>/", Borrarlugar.as_view(), name="lugarBorrar"),
path('buscarlugares', lista_lugares, name='lista_lugares'),


#CRUD Agencia De Viajess:
path("agencia/lista/", ListaagenciaDeviajes.as_view(), name="agenciaDeviajesLista"),
path("agencia/<int:pk>/", DetalleagenciaDeviajes.as_view(), name="agenciaDeviajesDetalle"),  
path("agencia/crear/", CrearagenciaDeviajes.as_view(), name="agenciaDeviajesCrear"),
path("agencia/editar/<int:pk>/", ActualizaragenciaDeviajes.as_view(), name="agenciaDeviajesEditar"),
path("agencia/borrar/<int:pk>/", BorraragenciaDeviajes.as_view(), name="agenciaDeviajesBorrar"),




#CRUD Hoteles:
path("hoteles/lista/", Listahotel.as_view(), name="hotelLista"),
path("hoteles/<int:pk>/", Detallehotel.as_view(), name="hotelDetalle"),  
path("hoteles/crear/", Crearhotel.as_view(), name="hotelCrear"),
path("hoteles/editar/<int:pk>/", Actualizarhotel.as_view(), name="hotelEditar"),
path("hoteles/borrar/<int:pk>/", Borrarhotel.as_view(), name="hotelBorrar"),


    
    
    
]
