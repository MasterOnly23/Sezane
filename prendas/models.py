from django.db import models

# Create your models here.

class Prendas(models.Model):
    tallas = (('S','S'),
              ('M','M'),
              ('L','L'),
              ('XL','XL'),
              ('XXL','XXL'),
              )
    
    prendas = (('Tanga','Tanga'),
              ('Cachetero','Chachetero'),
              ('Top Clasico','Top Clasico'),
              ('Top Deportivo','Top Deportivo'),
              ('Short','Short'),
              ('Duo Clasico','Duo Clasico'),
              ('Duo Deportivo','Duo Deportivo'),
              ('Duo Short','Duo Short'),
              ('Trio','Trio'),
              ('Boxer','Boxer')
              )

    prenda = models.CharField(max_length=50, choices=prendas)
    talla = models.CharField(max_length=3, choices=tallas)
    color = models.CharField(max_length=50)
    cantidad = models.IntegerField()