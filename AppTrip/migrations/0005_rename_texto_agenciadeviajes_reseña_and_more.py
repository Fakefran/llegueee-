# Generated by Django 5.0 on 2024-02-19 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrip', '0004_delete_viajesros_agenciadeviajes_texto_lugar_texto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenciadeviajes',
            old_name='texto',
            new_name='reseña',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='texto',
            new_name='reseña',
        ),
        migrations.RenameField(
            model_name='lugar',
            old_name='texto',
            new_name='reseña',
        ),
    ]
