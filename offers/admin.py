from django.contrib import admin
from models import *
# Register your models here.
class offer_typeAdmin(admin.ModelAdmin):
	list_display = ['offername','status']
	class Meta:
		model = offer_type

class offer_descriptionAdmin(admin.ModelAdmin):
	class Meta:
		model = offer_description

admin.site.register(offer_type,offer_typeAdmin)
admin.site.register(offer_description,offer_descriptionAdmin)