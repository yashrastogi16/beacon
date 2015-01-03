from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import *

print "hello"
@api_view(['GET','POST'])
def beacon_mac(request):
    if request.method == 'GET':
        mac_add = becon_mac.objects.all()
        serializer = becon_macSerializer(mac_add, many=True)
        return Response(serializer.data)