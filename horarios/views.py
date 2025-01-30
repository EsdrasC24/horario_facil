from django.shortcuts import render, redirect, get_object_or_404
from .models import Horario
from .forms import HorarioForm

# Listar todos los horarios
def lista_horarios(request):
    horarios = Horario.objects.all()
    return render(request, 'horarios/lista.html', {'horarios': horarios})

# Crear un nuevo horario
def crear_horario(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_horarios')
    else:
        form = HorarioForm()
    return render(request, 'horarios/crear.html', {'form': form})

# Ver detalles de un horario
def detalle_horario(request, id):
    horario = get_object_or_404(Horario, id=id)
    return render(request, 'horarios/detalle.html', {'horario': horario})

# Editar un horario
def editar_horario(request, id):
    horario = get_object_or_404(Horario, id=id)
    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('lista_horarios')
    else:
        form = HorarioForm(instance=horario)
    return render(request, 'horarios/editar.html', {'form': form})

# Eliminar un horario
def eliminar_horario(request, id):
    horario = get_object_or_404(Horario, id=id)
    if request.method == 'POST':
        horario.delete()
        return redirect('lista_horarios')
    return render(request, 'horarios/eliminar.html', {'horario': horario})
