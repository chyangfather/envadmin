# Create your views here.
from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from django.shortcuts import render_to_response

from models import *

class ResourceListView(ListView):
	#context_object_name = "publisher"
    model = Resource

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ResourceListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nodes'] = ResourceType.tree.all()
        return context
