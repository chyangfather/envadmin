from django.db import models

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=255)
	
	#class Meta:
	#	abstract = True
	def __unicode__(self):
		return self.name


class Person(Subject):	                          
	
	mail = models.EmailField()

	isInner = models.BooleanField()

	company = models.ForeignKey("OrgUnit",null=True)


class OrgUnit(Subject):
	pass
	
