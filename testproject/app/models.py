from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    city = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name