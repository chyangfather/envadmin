# coding=utf-8
from django.db import models
from subject.models import Subject,Person
#import subject

class Dictionary(models.Model):
	dict_key = models.CharField(max_length=255)
	dict_value = models.CharField(max_length=255)
		
class Project(Subject):
	plan_date = models.DateField()
	finished_date = models.DateField(null=True,blank=True)
	tag = models.ForeignKey('Dictionary',related_name='tag',null=True)
	state = models.ForeignKey('Dictionary',related_name='state')
	members = models.ManyToManyField(Person, through='JoinProject')
	def managers(self):
		return JoinProject.objects.filter(project=self,role=12)
		

	

class JoinProject(models.Model):
	person = models.ForeignKey('subject.Person')
	project = models.ForeignKey('Project')
	role = models.ForeignKey('Dictionary')
	
class ResManager(models.Model):
	pass