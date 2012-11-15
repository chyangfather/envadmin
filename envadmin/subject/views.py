# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

def partners(request):
	#return HttpResponse("hello, index!")
	return render_to_response('partners.html', {"project_list":Organization.objects.all()})