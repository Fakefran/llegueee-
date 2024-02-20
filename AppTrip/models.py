from django.db import models
from django.contrib.auth.models import User


    
class lugar(models.Model):
    destino = models.CharField(max_length=250)
    tipodeclima = models.CharField(max_length=250)
    reseña = models.TextField(default="Contanos tu experiencia")
    imagen = models.ImageField(upload_to='imagenes_lugares/', null=True, blank=True)
    

    
    
class agenciaDeviajes(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = models.IntegerField()
    email = models.EmailField()
    reseña = models.TextField(default="Dejano tu reseña")
    
    
class hotel(models.Model):
    nombre = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    calle= models.IntegerField()
    numero = models.IntegerField()
    email= models.EmailField()
    telefono = models.IntegerField()     
    reseña = models.TextField(default="Ingrese la reseña")
  
    
    
    
    



class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    
    class Meta:
        
        verbose_name = "Avatar"
        verbose_name_plural = "Avatars"
        
        
        



