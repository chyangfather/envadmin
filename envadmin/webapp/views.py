# coding=utf-8
from django.shortcuts import render_to_response,render
from django.contrib.auth import authenticate,login,logout

def general_form(request,formClass):

    if request.method == 'POST': # If the form has been submitted...
        form = formClass(request.POST) # A form bound to the POST data
        print form
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save(request=request)
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
            return render(request, 'parts/popup_form.html', {
                'form': form,
                'path': request.path,
                'global_errors': form.errors.get('__all__'),
            })
    else:
        form = formClass() # An unbound form
    

    return render(request, 'parts/popup_form.html', {
            'form': form,
            'path': request.path,
            'global_errors': form.errors.get('__all__'),
        })
   
def index(request):
	#return HttpResponse("hello, index!")
	return render_to_response('index.html', locals())

def login_view(request):    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    request.session['user']=user
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



from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from serializers import UserSerializer, GroupSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })

class UserList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = User
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Group
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Group
    serializer_class = GroupSerializer