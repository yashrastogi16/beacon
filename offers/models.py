from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime

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

