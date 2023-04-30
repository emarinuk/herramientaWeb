from django.contrib import admin

from biblioteca.models import Publicacion, Autor, Idioma, Editorial
# Register your models here.
admin.site.register(Publicacion)
admin.site.register(Idioma)
admin.site.register(Editorial)
admin.site.register(Autor)
