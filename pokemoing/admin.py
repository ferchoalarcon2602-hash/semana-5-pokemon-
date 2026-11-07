from django.contrib import admin

# Register your models here.
from .models import pokemon, gimnasio, entrenadores

admin.site.register(pokemon)
admin.site.register(gimnasio)
admin.site.register(entrenadores)
