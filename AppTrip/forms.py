from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User
from AppTrip.models import *






class UsuarioRegistro(UserCreationForm):
    username = forms.CharField(label= "Usuario")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", ]
        
class formularioEditar(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
    
        model = User
        fields = [ "email", "first_name", "last_name", "password1", "password2", ]
        
        

class AvatarFormulario(forms.ModelForm):
    
    
    class Meta:
        model = Avatar
        fields = ["imagen"]   
        

class BuscarLugarForm(forms.Form):
    busqueda = forms.CharField(label='Buscar lugar', max_length=100)
    
 