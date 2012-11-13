from django.db import models
from subject.models import Person
# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=255)
	manager = models.ForeignKey("Person", blank=True, null=True, related_name="manager")
	