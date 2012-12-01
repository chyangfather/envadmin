from rest_framework import serializers
from models import *

#class RequestSerializer()
class RequestSerializer(serializers.HyperlinkedModelSerializer):
	#type = serializers.RelatedField()
	class Meta:
		model = Request
		fields = ('subject', 'res_type', 'days_limit', 'end_date','comment')