
from django.urls import path
from . import views

urlpatterns = [

    # INICIO
    path('', views.index, name='index'),

    # POKEMON
    path('pokemon/', views.lista_pokemon, name='pokemo'),
    path('pokemon/agregar/', views.crear_pokemon, name='crear_pokemon'),
    path('pokemon/editar/<int:pk>/', views.editar_pokemon, name='editar_pokemon'),
    path('pokemon/eliminar/<int:pk>/', views.eliminar_pokemon, name='eliminar_pokemon'),

    # ENTRENADORES
    path('entrenadores/', views.lista_entrenadores, name='entrenadores'),
    path('entrenadores/agregar/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenadores/editar/<int:pk>/', views.editar_entrenador, name='editar_entrenador'),
    path('entrenadores/eliminar/<int:pk>/', views.eliminar_entrenador, name='eliminar_entrenador'),

    # GIMNASIOS
    path('gimnasios/', views.lista_gimnasios, name='gimnasios'),
    path('gimnasios/agregar/', views.crear_gimnasio, name='crear_gimnasio'),
    path('gimnasios/editar/<int:pk>/', views.editar_gimnasio, name='editar_gimnasio'),
    path('gimnasios/eliminar/<int:pk>/', views.eliminar_gimnasio, name='eliminar_gimnasio'),
    path('pokeapi/', views.buscar_pokemon, name='pokemon'),

]
