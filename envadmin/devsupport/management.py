# coding=utf-8
from django.dispatch import receiver
from django.db.models.signals import post_syncdb 

from django.contrib.auth import models as authmodels

'''
@receiver(post_syncdb, sender=authmodels)
def initdb():
	print 'initdb...'
	inner = authmodels.Group(name='内部员工')
	outer = authmodels.Group(name='外部人员')
	me = authmodels.User(username='wanghaikuo')
	me.groups.add(inner)
	inner.save()
	outer.save()
	me.save()

'''
