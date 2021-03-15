from django.db import models

# Create your models here.
class SuperHeroe(models.Model):
    nombre = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    poder = models.ForeignKey('SuperPoder', models.DO_NOTHING, db_column='poder', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_heroe'


class SuperPoder(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_poder'