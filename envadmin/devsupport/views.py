# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
def index(request):
	#return HttpResponse("hello, index!")
	return render_to_response('index.html', locals())

def projects(request):
	#return HttpResponse("hello, index!")
	return render_to_response('projects/all.html', {"project_list":Project.objects.all()})


def hello(request):
    return HttpResponse("hello, Django!")

