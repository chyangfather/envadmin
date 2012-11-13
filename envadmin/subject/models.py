from django.db import models

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		abstract = True



class Person(Subject):
	mail = models.EmailField()

class Project(Subject):
	pass


