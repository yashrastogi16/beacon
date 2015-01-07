from django import forms
from django.forms import ModelForm,PasswordInput
from models import *
from beacon_info.models import *
from offers.models import *

class MemberForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = members
		fields = '__all__'
class RoleForm(forms.ModelForm):
    class Meta:
        model = role
        fields = '__all__'
class StoreForm(forms.ModelForm):
	class Meta:
		model = store
		fields = '__all__'
class DepartmentForm(forms.ModelForm):
	class Meta:
		model = department
		fields = '__all__'

class Beacon_macForm(forms.ModelForm):
	class Meta:
		model = becon_mac
		fields = '__all__'

class OfferForm(forms.ModelForm):
	class Meta:
		model = offer
		fields = '__all__'

class Store_userForm(forms.ModelForm):
	class Meta:
		model = store_user
		fields = '__all__'