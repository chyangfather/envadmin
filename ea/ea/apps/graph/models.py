from django.db import models

# Create your models here.
class Graph(models.Model):
    graphml = models.TextField()
