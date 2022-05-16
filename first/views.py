from django.http import JsonResponse
from django.shortcuts import render

# Create your views here. Link to urls.py in sapi

#third part imports
from rest_framework.response import Response
from rest_framework.views import APIView

#POST, GET and other Methods will require authentication to work
from rest_framework.permissions import IsAuthenticated


from .selializer import FooSerializer
from .models import FooModel

#when receiving requests



class FooView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		query_set = FooModel.objects.all()
		#use many=True if retrieving many sets
		serializa = FooSerializer(query_set, many=True)
		return Response(serializa.data)

	def post(self, request, *args, **kwargs):
		serializa =  FooSerializer(data=request.data)
		if serializa.is_valid():
			serializa.save()
			return Response(serializa.data)
		return Response(serializa.errors)