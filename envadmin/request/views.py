# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from resource.models import ResourceType
from rest_framework import generics
from serializers import *

def request_form_view(request):	
	restype = None
	if request.GET.has_key('type_id'):
		restype= ResourceType.objects.get(id=request.GET['type_id'])
	return render_to_response('parts/request_form.html', {"restype":restype})


def projects(request):
	#return HttpResponse("hello, index!")
	print request.GET['mine']
	return render_to_response('projects/all.html', {"project_list":Project.objects.all()})

def project_cards(request):
	return render_to_response('projects/cards.html', {"project_list":Project.objects.all()})	

def hello(request):
    return HttpResponse("hello, Django!")


