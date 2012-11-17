# Create your views here.
from django.conf.urls import patterns, url, include
from django.views.generic import ListView

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
def index(request):
	#return HttpResponse("hello, index!")
	nodes = ResourceType.tree.all()
	return render_to_response('resources.html', {'nodes': nodes, "project_list":Resource.objects.all()})