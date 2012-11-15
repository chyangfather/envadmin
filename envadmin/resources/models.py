# coding=utf-8
from django.db import models
from devsupport.models import Dictionary
from mptt.models import MPTTModel

# Create your models here.

class ResourceType(MPTTModel):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	host = models.ForeignKey("self", blank=True, null=True, related_name="parts")

	def __unicode__(self):
		return self.name

class AttributeDef(models.Model):
	# acquire attr请求属性;  manage attr管理属性，; host attr宿主属性，用于创建密码
	SCOPE_ACQUIRE = 'AQ'
	SCOPE_MANAGEMENT = 'MG'
	SCOPE_CREATE = 'CR'
	SCOPE_CHOICES = (
		(SCOPE_ACQUIRE, '请求'),
		(SCOPE_MANAGEMENT,'管理'),
		(SCOPE_CREATE,'创建'),
	)
	name = models.CharField(max_length=100)
	ref = models.ForeignKey('ResourceType',blank=True, null=True)
	res_type = models.ForeignKey('ResourceType',related_name='attributes')
	scope = models.CharField(max_length=2, choices=SCOPE_CHOICES, default=SCOPE_ACQUIRE)
	def __unicode__(self):
		return self.name

class Resource(MPTTModel):
	name = models.CharField(max_length=100)	
	type = models.ForeignKey('ResourceType')
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

	#subdomain = models.ForeignKey('Dictionary')
	def __unicode__(self):
		return self.name

class Attribute(models.Model):
	pass


