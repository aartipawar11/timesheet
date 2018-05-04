from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.users.models import UserProfile
import datetime 
from datetime import datetime, timedelta


class TaskView(APIView):

	def post(self,request):
		try:
			task_data = TaskSerializer(data=request.data)
			if not(task_data.is_valid()):
				return Response(task_data.errors)
			task_data.save()
			return Response(task_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

##Written By Ashwin
class EditTask(APIView):
		def get(self,request,user_id=None):

			try:
				if(user_id):
					get_data = Tasks.objects.get(pk=user_id)
					task_data = TaskSerializer(get_data)
					user_task_edit = {"usertasks":task_data.data}
					# return Response(user_dataa.data,status=status.HTTP_200_OK)
					return render(request,'edit_each_task.html',user_task_edit)
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
				user_tasks = TaskSerializer(get_data,data=request.data)
				print(user_tasks)
				if user_tasks.is_valid():
					user_tasks.save()
					return Response(user_tasks.data,status=status.HTTP_200_OK)			
			except:
				return Response("Error",status=status.HTTP_400_BAD_REQUEST)

## written by aarti
class UserTaskDatewise(APIView):
	def get(self,request,user_id=None):
		return render(request,'datewise_all_details.html')

	def post(self,request):
		usertasks = Tasks.objects.all()
		user_tasks = TaskSerializer(usertasks,many=True)
		return Response(user_tasks.data,status=status.HTTP_201_CREATED)
	
##Written By Ashwin
class CalculateHrs(APIView):
	def get(self,request,user_id):
		one_week_ago = datetime.today() - timedelta(days=7)
		get_week_tasks = Tasks.objects.filter(date__gte=one_week_ago,user_id=user_id)
		task_data = TaskSerializer(get_week_tasks,many=True)
		return Response(task_data.data,status=status.HTTP_201_CREATED)

	def post(self,request,user_id):
		one_month_ago = datetime.today() - timedelta(days=30)
		get_month_tasks = Tasks.objects.filter(date__gte=one_month_ago,user_id=user_id)
		month_data = TaskSerializer(get_month_tasks,many=True)
		return Response(month_data.data,status=status.HTTP_201_CREATED)