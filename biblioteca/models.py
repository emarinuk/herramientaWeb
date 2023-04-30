from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return self.apellidos + ",  " + self.nombre


class Idioma(models.Model):
    idioma = models.CharField(max_length=20)

    def __str__(self):
        return self.idioma


class Publicacion(models.Model):
    TIPOS = [("Libro", "Libro"),("Artículo", "Artículo")]
    tipo = models.CharField(verbose_name="Tipo de publicación", max_length=8, choices=TIPOS, default="Libro")
    titulo = models.CharField(max_length=100, verbose_name="Título")
    subtitulo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Subtítulo")
    revista = models.CharField(max_length=100, null=True, blank=True, verbose_name="Revista")
    volumen = models.IntegerField(null=True, blank=True, verbose_name="Volumen")
    numero = models.IntegerField(null=True, blank=True, verbose_name="Número")
    numero_paginas = models.IntegerField(null=True, blank=True, verbose_name="Número de páginas")
    mes_publicacion = models.IntegerField(null=True, blank=True, verbose_name="Més de publicación")
    year_publicacion = models.IntegerField(blank=True, verbose_name="Año de publicación")
    isbn10 = models.IntegerField(null=True, blank=True, verbose_name="ISBN 10")
    isbn13 = models.IntegerField(null=True, blank=True, verbose_name="ISBN 13")
    editorial = models.ForeignKey(Editorial, on_delete=DO_NOTHING, null=True, verbose_name="Casa editorial")  # check the on_delete
    autores = models.ManyToManyField(Autor, verbose_name="Autor/es")
    idioma = models.ForeignKey(Idioma, on_delete=DO_NOTHING, null=True, verbose_name="Idioma")  # check the on_delete
    portada = models.ImageField(null=True, blank=True, upload_to="portadas/")

    def __str__(self):
        return self.titulo

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.sl
