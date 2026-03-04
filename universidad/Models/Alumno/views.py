from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm


def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno_list.html', {'alumnos': alumnos})


def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumno_detail.html', {'alumno': alumno})


def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno:list')
    else:
        form = AlumnoForm()
    return render(request, 'alumno_form.html', {'form': form})


def alumno_edit(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno:list')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumno_form.html', {'form': form})


def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno:list')
    return render(request, 'alumno_confirm_delete.html', {'alumno': alumno})