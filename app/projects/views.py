from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
from django.http import Http404 
from app.projects.serializers import ProjectSerializer 
from app.projects.models import Projects

class ProjectView(APIView):
	# @csrf_exempt
	def post(self,request): 
		try: 
			project_data = ProjectSerializer(data=request.data) 
			if not(project_data.is_valid()): 
				return Response(project_data.errors,status=status.HTTP_404_NOT_FOUND) 
			project_data.save() 
			return Response(project_data.data,status=status.HTTP_201_CREATED) 
		except Exception as err: 
			print(err) 
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

	def get(self,request):
		try:
			project_Data= Projects.objects.all()
			project_data = ProjectSerializer(project_Data,many=True)
			print(project_data)
			return Response(project_data.data)
		except Exception as err: 
			print(err) 
			return Response("Error",status=status.HTTP_404_NOT_FOUND)