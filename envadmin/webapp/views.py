# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout

def index(request):
	#return HttpResponse("hello, index!")
	return render_to_response('index.html', locals())

def login_view(request):    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)    
        print request.user    
        return index(request)
    else:
        #验证失败，暂时不做处理
        return index(request)

def logout_view(request):
    logout(request)
    return index(request)