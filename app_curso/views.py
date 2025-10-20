from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Curso
from .forms import CursoForm

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index.html', {'cursos': cursos})

def ver_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    return render(request, 'cursos/ver.html', {'curso': curso})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al index después de crear
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CursoForm()

    return render(request, 'cursos/agregar.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            # Redirige al index después de editar
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CursoForm(instance=curso)

    return render(request, 'cursos/editar.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    if request.method == 'POST':
        curso.delete()
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))
