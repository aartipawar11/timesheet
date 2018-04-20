from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.serializers import TaskSerializer


class TaskView(APIView):
	
	def post(self,request):
		try:
			# import pdb;pdb.set_trace();
			task_data = TaskSerializer(data=request.data)
			if not(task_data.is_valid()):
				return Response(task_data.errors)
			task_data.save()
			return Response(task_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

	
	
	def put(self,request,user_id):
		try:
			# user_id = request.POST.get('id')
			get_data = Tasks.objects.get(pk=user_id)
			user_tasks = TaskSerializer(get_data,data=request.data)
			# print(user_tasks)
			if user_tasks.is_valid():
				user_tasks.save()
				return Response(user_tasks.data,status=status.HTTP_200_OK)
			
			# return Response("user_tasks.data")
		except:
			return Response("Error",status=status.HTTP_400_BAD_REQUEST)