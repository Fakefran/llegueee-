# Generated by Django 5.0 on 2024-02-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrip', '0003_remove_hotel_fecha_publicacion_remove_hotel_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='viajesros',
        ),
        migrations.AddField(
            model_name='agenciadeviajes',
            name='texto',
            field=models.TextField(default='Dejano tu reseña'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='texto',
            field=models.TextField(default='Contanos tu experiencia'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='texto',
            field=models.TextField(default='Ingrese la reseña'),
        ),
    ]