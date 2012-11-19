# Create your views here.
from django.conf.urls import patterns, url, include
from django.views.generic import ListView,DetailView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

def catalogs(request,pk=''):
	print 'type_id='+pk
	#print request.GET.has_key('type_id')
	#return HttpResponse("hello, Django!")
	view = None
	if len(pk)==0:
		view = ResourceTypeListView.as_view()
	else:
		view = ResourceDetailView.as_view()

	return view(request,pk=pk)
	

class ResourceTypeListView(ListView):
	#context_object_name = "publisher"
    model = ResourceType

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ResourceTypeListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nodes'] = ResourceType.tree.all()
        return context

class ResourceDetailView(DetailView):
	model = ResourceType

	def get_context_data(self, **kwargs):
		context = super(ResourceDetailView, self).get_context_data(**kwargs)
		context['nodes'] = ResourceType.tree.all()
		return context


