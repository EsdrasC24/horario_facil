from django.shortcuts import render, redirect, get_object_or_404
from .models import Asignatura
from .forms import AsignaturaForm

#TODO: incluir @login_required para proteger las rutas
# Listar todas las asignaturas
def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas/lista.html', {'asignaturas': asignaturas})

# Crear una nueva asignatura
def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'asignaturas/crear.html', {'form': form})

# Ver detalles de una asignatura
def detalle_asignatura(request, id):
    asignatura = get_object_or_404(Asignatura, id=id)
    return render(request, 'asignaturas/detalle.html', {'asignatura': asignatura})

# Editar una asignatura
def editar_asignatura(request, id):
    asignatura = get_object_or_404(Asignatura, id=id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'asignaturas/editar.html', {'form': form})

# Eliminar una asignatura
def eliminar_asignatura(request, id):
    asignatura = get_object_or_404(Asignatura, id=id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'asignaturas/eliminar.html', {'asignatura': asignatura})
