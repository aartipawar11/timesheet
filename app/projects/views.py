from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.projects.serializers import ProjectSerializer



class ProjectView(APIView):
	
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

