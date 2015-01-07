from django.forms import widgets
from rest_framework import serializers
from rest_framework.fields import Field
from models import *
from offers.models import *

# Mac Address of device and department id
class storeSerializer(serializers.ModelSerializer):
	class Meta:
		model = store
		fields = ('store_name','store_id')

class departmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = department
		fields = ('department_name','department_id','store')

class becon_macSerializer(serializers.ModelSerializer):
	class Meta:
		model = becon_mac
		fields = ('becon_id','department')

class offerSerializer(serializers.ModelSerializer):
	class Meta:
		model = offer
		fields = ('offer_code','store_code','entry_exit_type','offername','min_stay_time','description','membership','start_time','end_time')