from django.shortcuts import render, get_object_or_404, redirect
from .models import InscripcionAlumno
from .forms import InscripcionAlumnoForm


def inscripcion_list(request):
    inscripciones = InscripcionAlumno.objects.all()
    return render(request, 'inscripcion_list.html', {'inscripciones': inscripciones})


def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionAlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_list')
    else:
        form = InscripcionAlumnoForm()

    return render(request, 'inscripcion_form.html', {'form': form})


def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)

    if request.method == 'POST':
        form = InscripcionAlumnoForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_list')
    else:
        form = InscripcionAlumnoForm(instance=inscripcion)

    return render(request, 'inscripcion_form.html', {'form': form})


def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)

    if request.method == 'POST':
        inscripcion.delete()
        return redirect('inscripcion_list')

    return render(request, 'inscripcion_confirm_delete.html', {'inscripcion': inscripcion})