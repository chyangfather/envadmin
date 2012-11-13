# coding=utf-8
from django.db import models
#import subject
# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=255)
	plan_end = models.DateField()
	is_finished = models.BooleanField()
	

class JoinProject(models.Model):
	ROLE_CHOICES = (  
        (u'DEV', u'开发人员'),  
        (u'USR', u'用户'),
        (u'MGR', u'管理员'),  
    )   
	person = models.ForeignKey('subject.Person')
	project = models.ForeignKey('Project')
	role = models.CharField(max_length=3, choices=ROLE_CHOICES)
	
class ResManager(models.Model):
	pass