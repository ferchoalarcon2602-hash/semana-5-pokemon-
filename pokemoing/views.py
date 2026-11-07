
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import pokemon, entrenadores, gimnasio
from .forms import PokemonForm, EntrenadorForm, GimnasioForm
import pokebase as pb 


# =====================================
# INICIO
# =====================================

def index(request):

    pokemones = pokemon.objects.all()
    lista_entrenadores = entrenadores.objects.all()
    lista_gimnasios = gimnasio.objects.all()

    return render(request, 'pokemoing/index.html', {
        'pokemones': pokemones,
        'entrenadores': lista_entrenadores,
        'gimnasios': lista_gimnasios
    })


# =====================================
# CRUD POKEMON
# =====================================

def lista_pokemon(request):

    lista = pokemon.objects.all()

    return render(request, 'pokemoing/pokemon.html', {
        'objetos': lista,
        'tipo': 'pokemon',
        'titulo': 'Mis Pokémon',
        'crear_url': 'crear_pokemon',
        'editar_url': 'editar_pokemon',
        'eliminar_url': 'eliminar_pokemon'
    })


def crear_pokemon(request):

    formulario = PokemonForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pokémon creado correctamente.')
            return redirect('pokemon')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Agregar Pokémon',
        'volver_url': 'pokemon'
    })
    


def editar_pokemon(request, pk):

    objeto = get_object_or_404(pokemon, pk=pk)

    formulario = PokemonForm(request.POST or None,request.FILES or None, instance=objeto)

    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            messages.success(request, 'Pokémon actualizado correctamente.')

            return redirect('pokemon')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Editar Pokémon',
        'volver_url': 'pokemon'
    })


def eliminar_pokemon(request, pk):

    objeto = get_object_or_404(pokemon, pk=pk)

    if request.method == 'POST':

        objeto.delete()

        messages.success(request, 'Pokémon eliminado correctamente.')

        return redirect('pokemon')

    return render(request, 'pokemoing/eliminar.html', {
        'objeto': objeto,
        'titulo': 'Eliminar Pokémon',
        'volver_url': 'pokemon'
    })


# =====================================
# CRUD ENTRENADORES
# =====================================

def lista_entrenadores(request):

    lista = entrenadores.objects.all()

    return render(request, 'pokemoing/entrenadores.html', {
        'objetos': lista,
        'tipo': 'entrenadores',
        'titulo': 'Mis Entrenadores',
        'crear_url': 'crear_entrenador',
        'editar_url': 'editar_entrenador',
        'eliminar_url': 'eliminar_entrenador'
    })


def crear_entrenador(request):

    formulario = EntrenadorForm(request.POST or None)

    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            messages.success(request, '¡Entrenador registrado correctamente!')

            return redirect('entrenadores')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Agregar Entrenador',
        'volver_url': 'entrenadores'
    })


def editar_entrenador(request, pk):

    objeto = get_object_or_404(entrenadores, pk=pk)

    formulario = EntrenadorForm(request.POST or None, instance=objeto)

    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            messages.success(request, 'Entrenador actualizado correctamente.')

            return redirect('entrenadores')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Editar Entrenador',
        'volver_url': 'entrenadores'
    })


def eliminar_entrenador(request, pk):

    objeto = get_object_or_404(entrenadores, pk=pk)

    if request.method == 'POST':

        objeto.delete()

        messages.success(request, 'Entrenador eliminado correctamente.')

        return redirect('entrenadores')

    return render(request, 'pokemoing/eliminar.html', {
        'objeto': objeto,
        'titulo': 'Eliminar Entrenador',
        'volver_url': 'entrenadores'
    })


# =====================================
# CRUD GIMNASIOS
# =====================================

def lista_gimnasios(request):

    lista = gimnasio.objects.all()

    return render(request, 'pokemoing/gimnasio.html', {
        'objetos': lista,
        'tipo': 'gimnasios',
        'titulo': 'Mis Gimnasios',
        'crear_url': 'crear_gimnasio',
        'editar_url': 'editar_gimnasio',
        'eliminar_url': 'eliminar_gimnasio'
    })


def crear_gimnasio(request):

    formulario = GimnasioForm(request.POST or None)

    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            messages.success(request, '¡Gimnasio creado correctamente!')

            return redirect('gimnasios')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Agregar Gimnasio',
        'volver_url': 'gimnasios'
    })


def editar_gimnasio(request, pk):

    objeto = get_object_or_404(gimnasio, pk=pk)

    formulario = GimnasioForm(request.POST or None, instance=objeto)

    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            messages.success(request, 'Gimnasio actualizado correctamente.')

            return redirect('gimnasios')

    return render(request, 'pokemoing/formulario_crud.html', {
        'formulario': formulario,
        'titulo': 'Editar Gimnasio',
        'volver_url': 'gimnasios'
    })


def eliminar_gimnasio(request, pk):

    objeto = get_object_or_404(gimnasio, pk=pk)

    if request.method == 'POST':

        objeto.delete()

        messages.success(request, 'Gimnasio eliminado correctamente.')

        return redirect('gimnasios')

    return render(request, 'pokemoing/eliminar.html', {
        'objeto': objeto,
        'titulo': 'Eliminar Gimnasio',
        'volver_url': 'gimnasios'
    })


def buscar_pokemon(request):

    pokemon = None
    error = None

    if request.method == "POST":

        nombre = request.POST.get("nombre", "").strip().lower()

        if nombre:

            try:
                # Consultar Pokémon mediante Pokebase
                pokemon_api = pb.pokemon(nombre)

                pokemon = {
                    "nombre": pokemon_api.name,
                    "id": pokemon_api.id,
                    "altura": pokemon_api.height / 10,
                    "peso": pokemon_api.weight / 10,
                    "imagen": pokemon_api.sprites.front_default,
                    "experiencia": pokemon_api.base_experience,
                    "tipos": [
                        tipo.type.name
                        for tipo in pokemon_api.types
                    ],
                }

            except Exception:
                error = "No se encontró el Pokémon. Intenta nuevamente."

        else:
            error = "Escribe el nombre de un Pokémon."

    return render(request, "pokemoing/pokeapi.html", {
        "pokemon": pokemon,
        "error": error
    })
