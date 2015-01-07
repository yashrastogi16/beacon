from django.contrib import admin
from models import *

class store_userAdmin(admin.ModelAdmin):
	list_display = ['firstname','user_id']
	class Meta:
		model = store_user

class membersAdmin(admin.ModelAdmin):
	list_display = ['username','user_id']
	class Meta:
		model = members

class roleAdmin(admin.ModelAdmin):
	list_display = ['rolename']
	class Meta:
		model = role
class feedbackAdmin(admin.ModelAdmin):
	list_display = ['user','feedback']
	class Meta:
		model = feedback

admin.site.register(store_user,store_userAdmin)
admin.site.register(members,membersAdmin)
admin.site.register(role,roleAdmin)
admin.site.register(feedback,feedbackAdmin)