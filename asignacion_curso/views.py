from django.shortcuts import render, redirect, get_object_or_404
from .models import AsignacionCurso
from .forms import AsignacionCursoForm

def asignacion_list(request):
    asignaciones = AsignacionCurso.objects.all().order_by('id')
    return render(request, 'asignacion_list.html', {'asignaciones': asignaciones})

def asignacion_create(request):
    if request.method == 'POST':
        form = AsignacionCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignacion:list')
    else:
        form = AsignacionCursoForm()
    return render(request, 'asignacion_form.html', {'form': form})

def asignacion_edit(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    if request.method == 'POST':
        form = AsignacionCursoForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            return redirect('asignacion:list')
    else:
        form = AsignacionCursoForm(instance=asignacion)
    return render(request, 'asignacion_form.html', {'form': form})

def asignacion_delete(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('asignacion:list')
    return render(request, 'asignacion_confirm_delete.html', {'asignacion': asignacion})