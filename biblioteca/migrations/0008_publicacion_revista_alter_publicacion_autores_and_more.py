# Generated by Django 4.2 on 2023-04-29 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_alter_publicacion_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='revista',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Revista'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='autores',
            field=models.ManyToManyField(to='biblioteca.autor', verbose_name='Autores'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.editorial', verbose_name='Casa editorial'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='biblioteca.idioma', verbose_name='Idioma'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='isbn10',
            field=models.IntegerField(blank=True, null=True, verbose_name='ISBN 10'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='isbn13',
            field=models.IntegerField(blank=True, null=True, verbose_name='ISBN 13'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='mes_publicacion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Més de publicación'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='numero',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='numero_paginas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de páginas'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='tipo',
            field=models.CharField(choices=[('Libro', 'Libro'), ('Artículo', 'Artículo')], default='Libro', max_length=8, verbose_name='Tipo de publicación'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='year_publicacion',
            field=models.IntegerField(blank=True, verbose_name='Año de publicación'),
        ),
    ]
