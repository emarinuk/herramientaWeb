# Generated by Django 4.2 on 2023-04-28 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('pais', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(blank=True, max_length=100)),
                ('numero', models.IntegerField(blank=True)),
                ('numero_paginas', models.IntegerField(blank=True)),
                ('mes_publicacion', models.IntegerField(blank=True)),
                ('year_publicacion', models.IntegerField(blank=True)),
                ('isbn10', models.IntegerField(blank=True, null=True)),
                ('isbn13', models.IntegerField(blank=True)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas/')),
                ('autores', models.ManyToManyField(to='biblioteca.autor')),
                ('editorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.editorial')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.idioma')),
            ],
        ),
    ]
