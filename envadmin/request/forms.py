# coding=utf-8
#from django import forms

#class RequestForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField()
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)
from models import *
from django.forms import *
from django_bootstrap.widgets import *
class RequestForm(ModelForm):
	days_limit = Spinner(label='期限',help_text='希望在几天内受理')
	
		
		
	class Meta:
		model = Request
		#fields = ('days_limit', 'end_date', 'comment')
		widgets = {
            'comment': Textarea(attrs={'cols': 120, 'rows': 8}),
        }
		