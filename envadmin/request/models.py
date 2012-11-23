# coding=utf-8
from django.db import models
from subject.models import Subject,Person
from resource.models import *
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


class Request(models.Model):
	subject = models.ForeignKey(Subject)
	res_type = models.ForeignKey('resource.ResourceType')
	days_limit = models.IntegerField()
	end_date = models.DateField()
	comment = models.TextField()
	
class RequestFactor(models.Model):
	request = models.ForeignKey(Request)
	key = models.ForeignKey('resource.AttributeDef')
	value = models.CharField(max_length=255)
	reference = models.ForeignKey('resource.Resource',blank=True)

class CompositeAcquireDef(models.Model):
	pass
class CompositeAcquire(models.Model):
	#组合请求，比如人员入场，项目等
	pass
	


	
