from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from push_notifications.models import GCMDevice
# GCMDevice viewsets
class GCMDeviceViewSet(viewsets.ModelViewSet):
	queryset = GCMDevice.objects.all()
	serializer_class = GCMDeviceSerializer

# api registering and Showing the registered device.
@api_view(['GET', 'POST'])
def gcmdevice_list(request):
    """
    List all Gcmdevice, or create a new snippet.
    """
    if request.method == 'GET':
        gcmdevice = GCMDevice.objects.all()
        serializer = GCMDeviceSerializer(gcmdevice, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GCMDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api for sending push notification to single device.
@api_view(['GET','POST'])
def pushnotify(request,registration_id,message):
    try:
        device = GCMDevice.objects.get(registration_id = registration_id)
    except Exception as e:
        print e
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = {}
        result = {}
        if device:
            device.send_message(str(message))
            data['msg'] = 'Message Sent'
            result['data'] = data
            result['code'] = 1
        else:
            data['msg'] = 'Message Not Sent'
            result['data'] = data
            result['code'] = 0
        return Response(result)



