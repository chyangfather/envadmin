# coding=utf-8
from django.db import models
from mptt.models import MPTTModel

# Create your models here.
class Subdomain(models.Model):
	name = models.CharField(max_length=100)
class ResourceType(models.Model):
	name = models.CharField(max_length=100)

class  ResourceAssociationType(MPTTModel):
	name = models.CharField(max_length=100)
	
		

class Resource(MPTTModel):
	SUBDOMAIN_CHOICES = (  
        (u'DEV', u'开发环境'),  
        (u'UAT', u'UAT环境'),
        (u'RUN', u'生产环境'),  
    )   

	type = models.ForeignKey('ResourceType')
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	Subdomain = models.CharField(max_length=3, choices=SUBDOMAIN_CHOICES)


