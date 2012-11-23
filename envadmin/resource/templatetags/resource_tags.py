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
	enb = len(resourcetype.resource_set.filter(state='ENB'))

	total = len(resourcetype.resource_set.all())
	for item in resourcetype.resource_set.all():
		print item.state
	if total==0:
		return '<div class="progress" style="margin:0px;"></div>'
	using = [use,out,unr,dis,enb]

	percents = [0,0,0,0,0]

	for index in range(len(percents)):
		percents[index] = using[index]*100/total

	percents[4] = 100-percents[0]-percents[1]-percents[2]-percents[3]
	print using,percents


	format = '''<div class="progress" style="margin:0px;">
	<div class="bar bar-primary" style="width: %f%%;">%d</div>
	<div class="bar bar-danger" style="width: %f%%;">%d</div>
	<div class="bar bar-warning" style="width: %f%%;">%d</div>
	<div class="bar bar-gray" style="width:%f%%;">%d</div>
	<div class="bar bar-success" style="width:%f%%;">%d</div>
	</div>'''

	return format % (percents[0],use,percents[1],out,percents[2],unr,percents[3],dis,percents[4],enb)


@register.simple_tag
def restype_having_bar(resourcetype,min_percent=10):
	enb = len(resourcetype.resource_set.filter(state='ENB'))
	total = len(resourcetype.resource_set.all())
	percent = 0
	if total > 0 :
		percent= enb*100/total
	return "#red 可用数：%d/%d(%d%%)#red" % (enb,total,percent)
