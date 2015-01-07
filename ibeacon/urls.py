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
    # Admin panel default.
    url(r'^admin/', include(admin.site.urls)),
    # Api's for different requirements.
    url(r'^gcmtest/',include(router.urls)),
    url(r'^gcmdevice_list/','push_notifications.views.gcmdevice_list',name='gcmdevice_list'),
    url(r'^beacon_mac/','beacon_info.views.beacon_mac',name='beacon_mac'),
    url(r'^offer_list/','beacon_info.views.offer_list',name='offer_list'),
    # For sending messages to different registered devices.
    url(r'^pushnotify/(?P<registration_id>.+)/(?P<message>.+)$','push_notifications.views.pushnotify',name='pushnotify'),
    #Template Based admin panel.
    url(r'^$','login.views.login',name='login'),# Admin Login
    url(r'^login/','login.views.login',name='login'),
    url(r'^logout/','login.views.logout',name='logout'),
    # Default Dashboard.
    url(r'^dashboard/','login.views.dashboard',name='dashboard'),
    # View Users and add them. 
    url(r'^viewuser/','login.views.userlist',name='userlist'),
    url(r'^adduser/','login.views.adduser', name='adduser'),
    # Add and view departments where the beacon's are to be installed.
    url(r'^adddepartment/','login.views.adddepartment', name='adddepartment'),
    url(r'^viewdepartment/','login.views.departmentlist',name='departmentlist'),
    # Add and view beacon devices.
    url(r'^addbeacon/','login.views.addbeacon', name='addbeacon'),
    url(r'^viewbeacon/','login.views.beaconlist',name='beaconlist'),
    # Add offers and Views offer.
    url(r'^addoffer/','login.views.addoffer', name='addoffer'),
    url(r'^viewoffer/','login.views.offerlist',name='offerlist'),
)
