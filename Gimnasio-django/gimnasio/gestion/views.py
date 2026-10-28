# Create your views here.

from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

from gestion.models import Miembro, Clase

# ======================================================
# FORMULARIOS AUTOMÁTICOS
# ======================================================
# Se crean formularios automáticamente desde los modelos
# EXCLUIMOS fecha_inscripcion porque se genera sola
MiembroForm = modelform_factory(Miembro,exclude=['fecha_inscripcion'])
ClaseForm = modelform_factory(Clase,exclude=[])

# ======================================================
# PÁGINA INICIAL
# ======================================================
def inicio(request):
    miembros = Miembro.objects.all()
    clases = Clase.objects.all()
    return render(request, 'gestion/inicio.html', {
        'miembros': miembros,
        'clases': clases
    })

# ======================================================
# MIEMBRO
# ======================================================
def nuevoMiembro(request):
    """
    Crea un nuevo miembro.
    fecha_inscripcion NO aparece en el formulario
    porque se guarda automáticamente.
    """
    if request.method == 'POST':
        formulario = MiembroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'gestion/miembros/nuevo.html', {'formulario': formulario})

    formulario = MiembroForm()
    return render(request, 'gestion/miembros/nuevo.html', {'formulario': formulario})


def editarMiembro(request, id):
    miembro = get_object_or_404(Miembro, pk=id)

    if request.method == 'POST':
        formulario = MiembroForm(request.POST, instance=miembro)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'gestion/miembros/editar.html', {'formulario': formulario})

    formulario = MiembroForm(instance=miembro)
    return render(request, 'gestion/miembros/editar.html', {'formulario': formulario})


def eliminarMiembro(request, id):
    miembro = get_object_or_404(Miembro, pk=id)

    if request.method == 'POST':
        miembro.delete()
        return redirect('inicio')

    return render(request, 'gestion/miembros/eliminar.html', {'miembro': miembro})


def detalleMiembro(request, id):
    """
    Muestra toda la información del miembro,
    incluyendo fecha_inscripcion.
    """
    miembro = get_object_or_404(Miembro, pk=id)
    return render(request, 'gestion/miembros/detalle.html', {'miembro': miembro})

# ======================================================
# CLASE
# ======================================================
def nuevaClase(request):
    if request.method == 'POST':
        formulario = ClaseForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'gestion/clases/nuevo.html', {'formulario': formulario})

    formulario = ClaseForm()
    return render(request, 'gestion/clases/nuevo.html', {'formulario': formulario})


def editarClase(request, id):
    clase = get_object_or_404(Clase, pk=id)

    if request.method == 'POST':
        formulario = ClaseForm(request.POST, instance=clase)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'gestion/clases/editar.html', {'formulario': formulario})

    formulario = ClaseForm(instance=clase)
    return render(request, 'gestion/clases/editar.html', {'formulario': formulario})


def eliminarClase(request, id):
    clase = get_object_or_404(Clase, pk=id)

    if request.method == 'POST':
        clase.delete()
        return redirect('inicio')

    return render(request, 'gestion/clases/eliminar.html', {'clase': clase})


def detalleClase(request, id):
    """
    Muestra todos los datos de la clase.
    """
    clase = get_object_or_404(Clase, pk=id)
    return render(request, 'gestion/clases/detalle.html', {'clase': clase})