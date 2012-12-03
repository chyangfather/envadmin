# coding=utf-8
<<<<<<< HEAD
from django import forms
from django.contrib.auth import authenticate,login,logout

class LoginForm(forms.Form):
	error_css_class = 'error'
	username = forms.CharField(label='用户名')
	password = forms.CharField(label='密码',widget=forms.PasswordInput)

	def save(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		return user
		#login(request, self.user)
		

	def clean(self):
		super(forms.Form, self).clean()
		if self.errors:
			return
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		self.user = user

		if user is None:
			raise forms.ValidationError("错误的用户名或密码!")
		
		
=======
#from django import forms

#class RequestForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField()
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)
from models import *
from django.forms import *
class LoginForm(Form):
	username = forms.CharField()
    password = forms.CharField()
>>>>>>> *) brahch
