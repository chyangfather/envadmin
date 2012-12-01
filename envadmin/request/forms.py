# coding=utf-8
#from django import forms

#class RequestForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField()
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)
from models import *
from django.forms import *
class RequestForm(ModelForm):
	class Meta:
		model = Request
		#fields = ('days_limit', 'end_date', 'comment')
		labels = {
			'days_limit':'期限',
		}
		widgets = {
            'comment': Textarea(attrs={'cols': 120, 'rows': 8}),
        }