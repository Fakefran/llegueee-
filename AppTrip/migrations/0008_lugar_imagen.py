# Generated by Django 5.0 on 2024-02-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrip', '0007_delete_imagenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_lugares/'),
        ),
    ]