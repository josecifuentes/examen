from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

class Empleado(models.Model):
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono_casa = models.CharField(max_length=200, blank=True, null=True)
    Dpi = models.CharField(max_length=200, blank=True, null=True)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):

        return '%s %s' % (self.Nombres, self.Apellidos)

class Cliente(models.Model):
    Nit = models.CharField(max_length=20, blank=True, null=True)
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s %s' % (self.Nit,self.Nombres, self.Apellidos)

class Plato(models.Model):
    Nombre  =   models.CharField(max_length=130)
    Precio = models.IntegerField()
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
	
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s %s' % (self.Nombre, self.Precio)


class Menu(models.Model):
    Nombre  =   models.CharField(max_length=130)
    Tipos = (
	    ('Desayuno', 'Desayuno'),
	    ('Almuerzo', 'Almuerzo'),
	    ('Refaccion', 'Refaccion'),
	    ('Cena', 'Cena'),
	    )
    Tipo_Menu = models.CharField(
	    max_length=10,
	    choices=Tipos,
	    default='Desayuno',
	    )
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s %s' % (self.Nombre, self.Tipo_Menu)


class Comida (models.Model):

    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Plato = models.ForeignKey(Plato, on_delete=models.CASCADE)


class ComidaInLine(admin.TabularInline):

    model = Comida

#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.

    extra = 1
class MenuAdmin(admin.ModelAdmin):

    inlines = (ComidaInLine,)


class PlatoAdmin (admin.ModelAdmin):

    inlines = (ComidaInLine,)