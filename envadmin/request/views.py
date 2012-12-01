# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from resource.models import ResourceType
from rest_framework import generics
from serializers import *
from django.template import RequestContext

from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import *

def request_form_view(request):	

	if request.method == 'GET':
		form = RequestForm()
		restype = None
		if request.GET.has_key('type_id'):
			restype= ResourceType.objects.get(id=request.GET['type_id'])
			req = Request(res_type=restype)
			form = RequestForm(instance=req)
		#return render_to_response('parts/request_form.html', c)
		return render(request, 'parts/popup_form.html', {
			'form': form,
		})
	elif request.method == 'POST':
		#print request.POST
		#return render_to_response('index.html', locals())
		form = RequestForm(request.POST)
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			form.save()
		return render(request, 'parts/popup_form.html', {
			'form': form,
		})
	


def projects(request):
	#return HttpResponse("hello, index!")
	print request.GET['mine']
	return render_to_response('projects/all.html', {"project_list":Project.objects.all()})

def project_cards(request):
	return render_to_response('projects/cards.html', {"project_list":Project.objects.all()})	

def hello(request):
    return HttpResponse("hello, Django!")


