from django.db import models 

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length=500)
    quantity = models.SmallIntegerField()