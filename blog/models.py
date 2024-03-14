from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.DecimalField(decimal_places=2, max_digits=5)
    is_stupid = models.BooleanField(default=True)
    email = models.EmailField()

    def __str__(self):   # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name

class Group(models.Model):  
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, related_name='groups')
    
    def __str__(self):
        return self.name
        
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType