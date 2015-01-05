from django.forms import widgets
from rest_framework import serializers
from rest_framework.fields import Field
from models import *

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
