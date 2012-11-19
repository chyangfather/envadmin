from django import template

register = template.Library()

@register.filter
def filter_resource_state(resources,state):
    return resources.filter(state=state)




@register.filter
def testfilter(value):
	return "hello, filter!"



#register.filter('test_filter',test_filter)

#print register.filters