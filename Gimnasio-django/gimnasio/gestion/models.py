from django.db import models
# Create your models here.


# ======================================================
# MODELO 1: MIEMBRO
# ======================================================
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # No se repiten correos)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    # Fecha en la que el miembro se inscribe en el gimnasio
    # auto_now_add guarda la fecha automáticamente al crear el registro
    fecha_inscripcion = models.DateField(auto_now_add=True)
    # Tipo de membresía (Ej: Mensual, Trimestral, Anual)
    tipo_membresia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ======================================================
# MODELO 2: CLASE
# ======================================================
class Clase(models.Model):
    # Nombre de la clase
    nombre_clase = models.CharField(max_length=100)
    descripcion = models.TextField()
    instructor = models.CharField(max_length=100)
    # Horario de la clase (Ej: Lunes 18:00)
    horario = models.CharField(max_length=100)
    capacidad_maxima = models.PositiveIntegerField()
    duracion_minutos = models.PositiveIntegerField()
    # Estado de la clase (activa o no)
    estado_activo = models.BooleanField(default=True)
    miembro = models.ForeignKey(Miembro,on_delete=models.CASCADE,  related_name='clases')# Si se elimina el miembro, se eliminan sus clases

    def __str__(self):
        return self.nombre_clase