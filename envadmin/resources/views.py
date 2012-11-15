# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

def resources(request):
	#return HttpResponse("hello, index!")
	nodes = ResourceType.tree.all()
	return render_to_response('resources.html', {'nodes': nodes, "project_list":Resource.objects.all()})