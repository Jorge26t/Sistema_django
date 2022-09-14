from pyexpat import model
from django.db import models
from datetime import datetime
#hacer esto es importante

#para la tabla tipo
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', default='Sin nombres', unique=True)

   # esto sirve para devolver employer
    def __str__(self):
        return self.name

    class Meta:
        # cuaod se registre la aplicacion en el modulo de administracion de django
        verbose_name = 'Tipos'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipos'
        #para ordenar ascendente, si es desendente solo poner un menor antes del id [-id]
        ordering = ['id']

# para la tbala categoria
class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', default='Sin nombres')

   # esto sirve para devolver employer
    def __str__(self):
        return self.name

    class Meta:
        # cuaod se registre la aplicacion en el modulo de administracion de django
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        db_table = 'Categoria'
        #para ordenar ascendente, si es desendente solo poner un menor antes del id [-id]
        ordering = ['id']

#tabla empleado esta relacionado con la table Type
class Empleado(models.Model):
    #relaciones
    categ = models.ManyToManyField(Categoria)
    type =  models.ForeignKey(Type, on_delete=models.CASCADE)

    names = models.CharField(max_length=200, verbose_name='Nombres', default='Sin nombres')
    dni = models.CharField(max_length=12, unique=True, verbose_name='Dni')
    date_joind = models.DateField(default=datetime.now, verbose_name='Fecha registro')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Fecha crear')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha actualizar')
    age = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%M/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%M/%d', null=True, blank=True)
    gender = models.CharField(max_length=50)

    # esto sirve para devolver employer
    def __str__(self):
        return self.names

    class Meta:
        # cuaod se registre la aplicacion en el modulo de administracion de django
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleado'
        db_table = 'Empleado'
        #para ordenar ascendente, si es desendente solo poner un menor antes del id [-id]
        ordering = ['id']





