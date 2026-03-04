from django.shortcuts import render, get_object_or_404, redirect
from .models import Catedratico
from .forms import CatedraticoForm

def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'catedratico_list.html', {'catedraticos': catedraticos})

def catedratico_detail(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    return render(request, 'catedratico_detail.html', {'catedratico': catedratico})

def catedratico_create(request):
    if request.method == 'POST':
        form = CatedraticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catedratico:list')
    else:
        form = CatedraticoForm()
    return render(request, 'catedratico_form.html', {'form': form})

def catedratico_edit(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        form = CatedraticoForm(request.POST, instance=catedratico)
        if form.is_valid():
            form.save()
            return redirect('catedratico:list')
    else:
        form = CatedraticoForm(instance=catedratico)
    return render(request, 'catedratico_form.html', {'form': form})

def catedratico_delete(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        catedratico.delete()
        return redirect('catedratico:list')
    return render(request, 'catedratico_confirm_delete.html', {'catedratico': catedratico})