# coding=utf-8
from django.db import models
from subject.models import Subject,Person
from resources.models import *
import datetime
#import subject

class Dictionary(models.Model):
	dict_key = models.CharField(max_length=255)
	dict_value = models.CharField(max_length=255)
		
class Project(Subject):
	plan_date = models.DateField()
	tag = models.ForeignKey('Dictionary',related_name='tag',null=True)
	state = models.ForeignKey('Dictionary',related_name='state')
	is_finished = models.BooleanField()
	#outputs = models.OneToMany	
	members = models.ManyToManyField(Person, through='JoinProject')
	def living_acquire(self):
		return self.acquire_set.filter(resource=None)

	def managers(self):
		return JoinProject.objects.filter(project=self,role=12)
	def delay(self):
		return self.plan_date < datetime.date.today()
	def __unicode__(self):
		return self.name
		

class JoinProject(models.Model):
	person = models.ForeignKey('subject.Person')
	project = models.ForeignKey('Project')
	role = models.ForeignKey('Dictionary')


class Acquire(models.Model):
	subject = models.ForeignKey(Subject)
	res_type = models.ForeignKey('resources.ResourceType')
	days_limit = models.IntegerField()
	resource = models.ForeignKey('resources.Resource',null=True)
	


	
