from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from biblioteca.models import Publicacion
from biblioteca.forms import FormularioLibro, FormularioArticulo, FormularioNuevoUsuario
from django.conf import settings


# Create your views here.


def nuevo_libro(request):
    formulario_publicacion = FormularioLibro
    if request.POST:
        formulario_publicacion = FormularioLibro(request.POST)
        if formulario_publicacion.is_valid() and user.is_authenticated:
            formulario_publicacion.save()
            return redirect(reverse('lista_publicaciones'))
    context = {"formulario": formulario_publicacion, "titulo_pagina": "Añadir libro", "etiqueta_boton": "Añadir libro"}
    return render(request, 'biblioteca/nueva_publicacion.html', context)


def nuevo_articulo(request):
    formulario_publicacion = FormularioArticulo
    if request.POST:
        formulario_publicacion = FormularioArticulo(request.POST)
        if formulario_publicacion.is_valid():
            formulario_publicacion.save()
            return redirect(reverse('lista_publicaciones'))
    context = {"formulario": formulario_publicacion, "titulo_pagina": "Añadir articulo",
               "etiqueta_boton": "Añadir artículo"}
    return render(request, 'biblioteca/nueva_publicacion.html', context)


@login_required(login_url='/')
def pagina_publicacion(request, my_id):
    publicacion = Publicacion.objects.get(id=my_id)
    context = {'publicacion': publicacion}
    try:
        if my_id == 0:
            return redirect(reverse('homepage'))
        return render(request, 'biblioteca/publicacion.html', context)
    except:
        return HttpResponseNotFound("<h3>404: Not Found</h3>")


def lista_publicaciones(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    lista_libros = Publicacion.objects.filter(tipo="Libro", ).order_by("titulo")
    lista_articulos = Publicacion.objects.filter(tipo="Artículo")
    # context = {'lista_libros': lista_libros}
    context = {'lista_libros': lista_libros, 'lista_articulos': lista_articulos}
    return render(request, 'biblioteca/lista_publicaciones.html', context)


def pagina_inicio(request):
    context = {}
    return render(request, 'biblioteca/home.html', context)


def register_user(request):
    formulario = FormularioNuevoUsuario()

    if request.method == "POST":
        formulario = FormularioNuevoUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect("/")

    context = {"formulario": formulario}
    return render(request, 'registration/registration.html', context)