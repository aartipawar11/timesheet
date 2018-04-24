from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django.views.generic import TemplateView
from django.shortcuts import render,redirect


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

class EditTask(APIView):
		def get(self,request,user_id=None):

			try:
				if(user_id):
					userprofilee = Tasks.objects.get(pk=user_id)
					user_dataa = TaskSerializer(userprofilee)
					usertaskedit = {"usertasks":user_dataa.data}
					# return Response(user_dataa.data,status=status.HTTP_200_OK)
					return render(request,'edit_each_task.html',usertaskedit)
			except:
				return Response("Error")
			return render(request,'edittask.html')

		def post(self,request):
			usertasks = Tasks.objects.all()
			user_tasks = TaskSerializer(usertasks,many=True)
			return Response(user_tasks.data,status=status.HTTP_201_CREATED)

		def put(self,request,user_id):
			try:
				get_data = Tasks.objects.get(pk=user_id)
				# print("inside get data")
				user_tasks = TaskSerializer(get_data,data=request.data)
				print(user_tasks)
				if user_tasks.is_valid():
					user_tasks.save()
					return Response(user_tasks.data,status=status.HTTP_200_OK)
				
				# return Response("user_tasks.data")
			except:
				return Response("Error",status=status.HTTP_400_BAD_REQUEST)



