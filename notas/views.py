from django.shortcuts import render, get_object_or_404, redirect
from .models import Notas
from .forms import NotasForm


def notas_list(request):
    notas = Notas.objects.all()
    return render(request, 'notas_list.html', {'notas': notas})


def notas_create(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notas_list')
    else:
        form = NotasForm()

    return render(request, 'notas_form.html', {'form': form})


def notas_edit(request, pk):
    nota = get_object_or_404(Notas, pk=pk)

    if request.method == 'POST':
        form = NotasForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('notas_list')
    else:
        form = NotasForm(instance=nota)

    return render(request, 'notas_form.html', {'form': form})


def notas_delete(request, pk):
    nota = get_object_or_404(Notas, pk=pk)

    if request.method == 'POST':
        nota.delete()
        return redirect('notas_list')

    return render(request, 'notas_confirm_delete.html', {'nota': nota})