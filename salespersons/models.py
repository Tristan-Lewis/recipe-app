from django.db import models

# Create your models here.

class Salesperson(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()

    def __str__(self):
        return str(self.name)