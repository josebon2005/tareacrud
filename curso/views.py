from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm


def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})


def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})


def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso_form.html', {'form': form})


def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso:list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso})