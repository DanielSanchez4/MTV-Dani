from django.db import models



# Create your models here.


class familia(models.Model):

    nombre = models.CharField(max_length=10)
    
    edad = models.IntegerField()

    fecha = models.DateField()
