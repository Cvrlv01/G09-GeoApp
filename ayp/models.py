from django.db import models


# Create your models here.
class Figura(models.Model):
    figura = models.ImageField(upload_to='static/imagen')


class Alumno(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    contrasena = models.CharField()
    ejercicios = models.ManyToManyField('Ejercicios', through='PuntajeEjercicios')
    rut = models.BigIntegerField(primary_key=True)


class Ejercicios(models.Model):
    Idejercicio = models.CharField()
    resolucion = models.TextField()


class Formulas(models.Model):
    formulas = models.CharField(max_length=100, primary_key=True)

    # poner nombre de las formulas trapecio, paralelogramo...

    def __str__(self):
        return self.name


class AlumnoEjercicio(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ejercicios = models


class Problemas(models.Model):
    resolucion = models.CharField()
    respuesta = models.TextField()


class Puntaje(models.Model):
    puntaje = models.CharField()
    puntajealumno = models.CharField()

class PuntajeEjercicios(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ejercicios = models.ForeingKey(Alumno, on_delete=models.CASCADE)
    puntaje = models.IntegerField()

    def __str__(self):
        return f"{self.alumno.nombre} - {self.ejercicios.nombre} - {self.puntaje}"

class Profesor(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    contraseña =

class PuntajeAlumno(models.Model):

