from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.serializers import TaskSerializer



class TaskView(APIView):
	
	def post(self,request):
		try:
			task_data = TaskSerializer(data=request.data)
			if not(task_data.is_valid()):
				return Response(task_data.errors,status=status.HTTP_404_NOT_FOUND)
			task_data.save()
			return Response(task_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

