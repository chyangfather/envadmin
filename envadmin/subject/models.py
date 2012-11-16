from django.db import models

# Create your models here.
class Subject(models.Model):
	#name = models.CharField(max_length=255)
	
	#class Meta:
	#	abstract = True
	pass

class Person(Subject):	                          
	name = models.CharField(max_length=255)
	mail = models.EmailField()

	isInner = models.BooleanField()

	company = models.ForeignKey("Organization",null=True)


class Organization(models.Model):
	name = models.CharField(max_length=255)
	#full_name = models.CharField(max_length=255,null=True)
	def __unicode__(self):
		return self.name

