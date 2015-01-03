from django.forms import widgets
from rest_framework import serializers
from models import *

# Mac Address of device and department id
class becon_macSerializer(serializers.ModelSerializer):
	class Meta:
		model = becon_mac
		fields = ('becon_id','department')