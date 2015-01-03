from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from push_notifications.views import *

router = routers.DefaultRouter()
router.register(r'GCMDevice',GCMDeviceViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibeacon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gcmtest/',include(router.urls)),
    url(r'^gcmdevice_list/','push_notifications.views.gcmdevice_list',name='gcmdevice_list'),
    url(r'^beacon_mac/','beacon_info.views.beacon_mac',name='beacon_mac'),
    url(r'^pushnotify/(?P<registration_id>.+)/(?P<message>.+)$','push_notifications.views.pushnotify',name='pushnotify'),
    url(r'^admin/', include(admin.site.urls)),
)
