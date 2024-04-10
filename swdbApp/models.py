from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100, null=True, blank=True)
    terrains = models.TextField()
    climates = models.TextField()