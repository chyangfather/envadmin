# coding=utf-8
from django.db import models
from request.models import Dictionary
from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.

class ResourceType(MPTTModel):
	name = models.CharField(max_length=100)
	parent = TreeForeignKey("self", blank=True, null=True, related_name="children")

	host = models.ForeignKey("self", blank=True, null=True, related_name="parts")
	sort = models.IntegerField()
	is_abstract = models.BooleanField()
	def __unicode__(self):
		return self.name
	class MPTTMeta:
		order_insertion_by = ['name']

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
	STATE_ENABLE = 'ENB'
	STATE_DISABLE = 'DIS'
	STATE_USING = 'BSY'
	STATES = (
		(STATE_ENABLE,'可用'),
		(STATE_DISABLE,'停用'),
		(STATE_USING,'使用中'),
	)
	TRANSITIONS = (
		('','from','to'),
	)
	name = models.CharField(max_length=100)	
	res_type = models.ForeignKey('ResourceType')
	parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
	state = models.CharField(max_length=3, choices=STATES, default=STATE_ENABLE)
	#subdomain = models.ForeignKey('Dictionary')
	def __unicode__(self):
		return self.name

class Attribute(models.Model):
	pass


