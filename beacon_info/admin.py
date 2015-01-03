from django.contrib import admin
from models import *

class storeAdmin(admin.ModelAdmin):
	list_display = ['store_name','store_id','address','createdat']
	class Meta:
		model = store

class departmentAdmin(admin.ModelAdmin):
	list_display = ['department_name','department_id','createdat']
	class Meta:
		model = department

class becon_macAdmin(admin.ModelAdmin):
	list_display = ['becon_id']
	class Meta:
		model = becon_mac

admin.site.register(store,storeAdmin)
admin.site.register(department,departmentAdmin)
admin.site.register(becon_mac,becon_macAdmin)