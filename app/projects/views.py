from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.projects.serializers import ProjectSerializer
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.projects.models import Projects
from django.contrib.auth.models import User

## written by aarti
class ProjectView(APIView):
	
	def post(self,request):
		try:
			project_data = ProjectSerializer(data=request.data)
			if not(project_data.is_valid()):
				return Response(project_data.errors)
			project_data.save()
			return Response(project_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error")


	def get(self,request,id):
		try:
			# if(project_id):
			# 	get_project_data = UserProfile.objects.get(pk=project_id)
			# 	project_data = ProjectSerializer(get_project_data)
			# else:
			get_project_data = Projects.objects.all()
			project_data = ProjectSerializer(get_project_data,many=True)
			return Response(project_data.data)
		except Exception as err: 
			print(err) 
			return Response("Error")

	def put(self,request,project_id):
		try:
			
			get_data = Projects.objects.get(pk=project_id)
			update_data = ProjectSerializer(get_data,data=request.data)
			print(update_data)
			if update_data.is_valid():
				update_data.save()
				return Response(update_data.data)
		except:
			return Response("Error")

