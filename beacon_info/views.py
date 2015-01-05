from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import *

# @api_view(['GET','POST'])
# def beacon_mac(request):
#     try:
#        	mac_add = becon_mac.objects.all()
#     except Exception as e:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#     	tcount = {}
#     	data = {}
#     	list1 = []
#         # serializer = becon_macSerializer(mac_add, many=True)
#         tcount['code'] = 1
#         for i in mac_add:
#         	data['becon_id'] = i.becon_id
#         	print data['becon_id']
#         	data['department'] = str(i.department)
#         	print data['department']
#         	dept = department.objects.get(department_name = i.department)
#         	data['store'] = str(dept.store)
#         	print data['store']
#         	tcount['data']= data
#         list1.append(tcount)
#     	return Response(list1)


# @api_view(['GET','POST'])
# def beacon_mac(request):
#     if request.method == 'GET':
#         mac_add = becon_mac.objects.all()
#         serializer = becon_macSerializer(mac_add, many=True)
#         return Response(serializer.data)

@api_view(['GET','POST'])
def beacon_mac(request):
	if request.method == 'GET':
		list1 = []
		mac_add = becon_mac.objects.all()
		dept = department.objects.all()
		stor = store.objects.all()
		bcount = {}
		bcount['code'] = 1
		list1.append(bcount)
		for i in mac_add:
			tcount = {}
			data = {}
			data['becon_id'] = str(i.becon_id)
			print data['becon_id']
			data['department_id'] = str(i.department)
			print data['department_id']
			for j in dept:
				if str(i.department) == str(j.department_name):
					data['store_id'] = str(j.store)
					print data['store_id']
				tcount['data'] = data
				tcount.update(tcount)
			list1.append(tcount)
		print list1			
		return Response(list1)