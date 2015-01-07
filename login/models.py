from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime
from beacon_info.models import *

STATUS_CHOICES = (
	('A','Active'),
	('I','Inactive'),
	)

GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'), 
		)
class store_user(models.Model):
	firstname = models.CharField('First Name', max_length=60)
	lastname = models.CharField('Last Name', max_length=60)
	user_id = models.CharField('User_ID', unique = True , max_length=50)
	password = models.CharField('Password',max_length=20)
	email_id = models.CharField('Email_ID', max_length=254,unique=True)
	store_admin = models.ForeignKey('beacon_info.store')
	isactive = models.BooleanField('Isactive',default=True)
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.user_id)

class members(models.Model):
	username = models.CharField('UserName', max_length=60, null=True)
	gender = models.CharField(max_length=10,)
	user_id = models.CharField('User_ID', max_length=50, blank=False, unique=True)
	password = models.CharField('Password', max_length=30)
	email_id = models.EmailField('Email_ID', max_length=254, null=False)
	resident_location = models.CharField('Resident Location', max_length=50)
	contact_no = models.CharField('Contact No.', max_length=30, blank=True)
	status = models.BooleanField('Is Active', default=True)
	role = models.ForeignKey('role')
	date_time=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.username)

class role(models.Model):
	rolename = models.CharField(max_length=30)        
	status = models.CharField(max_length=40, choices=STATUS_CHOICES)
	def __unicode__(self):
		return smart_unicode(self.rolename)

class feedback(models.Model):
	user = models.ForeignKey('members')
	feedback = models.TextField()
	createdat = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.user)

class store_userlogin(models.Model):
	username = models.CharField(max_length=30)
	userid = models.CharField(max_length=30)
	store = models.CharField(max_length=10)
	logintime  = models.DateTimeField()
	def __unicode__(self):
		return smart_unicode(self.userid)

class store_userlogout(models.Model):
	username = models.CharField(max_length=30)
	userid = models.CharField(max_length=30)
	store = models.CharField(max_length=10)
	logouttime  = models.DateTimeField() 
	def __unicode__(self):
		return smart_unicode(self.userid)  