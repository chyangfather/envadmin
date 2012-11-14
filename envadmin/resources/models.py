# coding=utf-8
from django.db import models
from devsupport.models import Dictionary
from mptt.models import MPTTModel

# Create your models here.

class ResourceType(models.Model):
	name = models.CharField(max_length=100)

class  ResourceAssociationType(MPTTModel):
	name = models.CharField(max_length=100)
	
		

class Resource(MPTTModel):
	type = models.ForeignKey('ResourceType')
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	#subdomain = models.ForeignKey('Dictionary')


