from django.shortcuts import render, get_object_or_404, redirect
from universidad.Models.Alumno.models import Curso  # <- IMPORT CORRECTO

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso_detail.html', {'curso': curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        creditos = request.POST.get('creditos')
        Curso.objects.create(nombre=nombre, creditos=creditos)
        return redirect('curso:list')
    return render(request, 'curso_form.html')

def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.nombre = request.POST.get('nombre')
        curso.creditos = request.POST.get('creditos')
        curso.save()
        return redirect('curso:list')
    return render(request, 'curso_form.html', {'curso': curso})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso:list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso})