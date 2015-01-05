from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime

# Create your models here.
class store(models.Model):
	store_name = models.CharField('Store Name',max_length=100)
	store_id = models.CharField('Store_ID', max_length=20, unique=True)
	store_email = models.EmailField('Email_ID', max_length=254)
	address = models.CharField('Address', max_length=250)
	country = models.CharField('Country', max_length=50)
	state = models.CharField('State', max_length=50)
	city = models.CharField('City',max_length=50)
	pincode = models.CharField('Pincode', max_length=15)
	contact_no = models.CharField('Contact', max_length=15)
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.id)

class department(models.Model):
	department_name = models.CharField('Department Name', max_length=50)
	department_id = models.CharField('Department_ID', max_length=50)
	store = models.ForeignKey('store')
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.department_name)

class becon(models.Model):
	uiid = models.CharField('Becon UIID', max_length=100)
	major_id = models.CharField('Major ID', max_length=100)
	minor_id = models.CharField('Minor ID', max_length=100)
	department = models.ForeignKey('Department', max_length=100)
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.uiid)

class becon_mac(models.Model):
	becon_id = models.CharField('Becon Mac ID', max_length=100, unique=True)
	department = models.ForeignKey('Department', max_length=100)
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.becon_id)
		
