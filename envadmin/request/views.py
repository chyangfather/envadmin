# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *


def projects(request):
	#return HttpResponse("hello, index!")
	print request.GET['mine']
	return render_to_response('projects/all.html', {"project_list":Project.objects.all()})

def project_cards(request):
	return render_to_response('projects/cards.html', {"project_list":Project.objects.all()})	

def hello(request):
    return HttpResponse("hello, Django!")

