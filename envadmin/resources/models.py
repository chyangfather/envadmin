# coding=utf-8
from django.db import models
from devsupport.models import Dictionary
from mptt.models import MPTTModel

# Create your models here.

class ResourceType(models.Model):
	name = models.CharField(max_length=100)
	
class  ResourceAssociationType(MPTTModel):
	name = models.CharField(max_length=100)
	
class AttributeDef(models.Model):
	# acquire attr请求属性;  manage attr管理属性，; host attr宿主属性，用于创建密码
	name = models.CharField(max_length=100)
	res_type = models.ForeignKey('ResourceType')

class Resource(MPTTModel):
	name = models.CharField(max_length=100)	
	type = models.ForeignKey('ResourceType')
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	#subdomain = models.ForeignKey('Dictionary')
	def __unicode__(self):
		return self.name

class Attribute(models.Model):
	pass


