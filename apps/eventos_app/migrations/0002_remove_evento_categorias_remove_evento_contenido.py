# Generated by Django 4.0.6 on 2022-09-01 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='contenido',
        ),
    ]
