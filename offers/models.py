from django.db import models
from django.utils.encoding import smart_unicode
from beacon_info.models import * 
from django.utils import timezone
from datetime import datetime

STATUS_CHOICES = (
	('1','Entry'),
	('0','Exit'),
	)
def number():
		no = offer.objects.count()
		if no == None:
			return 1
		else:
			return no + 1
# Create your models here.
class offer_type(models.Model):
	offername = models.CharField('Offer Name',max_length=30)        
	status = models.BooleanField('Is Active ',default=True)
	createdat = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.offername)

class offer_description(models.Model):
	offer = models.ForeignKey('offer_type')
	description = models.TextField()
	createdat = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.offer.offername)

class offer(models.Model):
	offer_code = models.CharField(max_length=50,default=number)
	store_code = models.ForeignKey('beacon_info.store')
	entry_exit_type = models.CharField(max_length=50, choices=STATUS_CHOICES)
	offername = models.CharField(max_length=100, null=True)
	min_stay_time = models.CharField(max_length=20, blank=True)
	description = models.TextField()
	membership = models.CharField(max_length=5, default=1)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	createdat =models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.offername)

