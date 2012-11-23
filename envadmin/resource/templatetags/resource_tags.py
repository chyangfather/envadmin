# coding=utf-8
from django import template

register = template.Library()

@register.filter
def filter_resource_state(resources,state):
	return resources.filter(state=state)




@register.filter
def testfilter(value):
	return "hello, filter!"


@register.simple_tag
def restype_using_bar(resourcetype,min_percent=6):
	
	#使用+超时+未注册+停用

	use = len(resourcetype.resource_set.filter(state='USE'))
	out = len(resourcetype.resource_set.filter(state='OUT'))
	unr = len(resourcetype.resource_set.filter(state='UNR'))
	dis = len(resourcetype.resource_set.filter(state='DIS'))
	total = use+out+unr+dis
	using = [use,out,unr,dis]




	

	return using

@register.simple_tag
def restype_having_bar(resourcetype,min_percent=10):
	total = len(resourcetype.resource_set.all())
	if total ==0:
		return '<div class="progress" style="margin:0px;width:80%"></div>0/0'

	enb = len(resourcetype.resource_set.filter(state='ENB'))

	using = (total-enb)/total * 100

	
	if using<min_percent:
		using = min_percent
	
	style = 'success'
	if using>=90:
		style = 'danger'

	if using>80 and using<90:
		style = 'warning'

	width = using
	if width<min_percent:
		width = min_percent

	format = '''<div id="tooltip" class="progress" style="margin:0px;width:80%%">
				<div title="abcabc" class="bar bar-%s" style="width:%d%%;">%d %%</div>				
			</div>%d / %d'''
	return format % (style,width,using ,total-enb,total)
