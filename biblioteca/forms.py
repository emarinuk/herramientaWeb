from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from biblioteca.models import Publicacion


class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ["subtitulo", "numero_paginas", "isbn10", "isbn13", "portada"]


class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ["numero", "mes_publicacion", "revista", "volumen"]


class FormularioNuevoUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Enter"

    def clean_username(self):
        nuevo_usuario = self.cleaned_data['username'].lower()
        contador = User.objects.filter(username=nuevo_usuario)
        if contador.count():
            raise forms.ValidationError("User already exists!")
        return nuevo_usuario

    def clean_email(self):
        nuevo_email = self.cleaned_data['email'].lower()
        contador = User.objects.filter(email=nuevo_email)
        if contador.count():
            raise forms.ValidationError("Email already exists!")
        return nuevo_email

    def clean_password2(self):
        nuevo_password1 = self.cleaned_data['password1']
        nuevo_password2 = self.cleaned_data['password2']
        if nuevo_password2 and nuevo_password1 and nuevo_password1 != nuevo_password2:
            raise forms.ValidationError("Error en las passwords")
        return nuevo_password2

