from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from app.tasks.models import Tasks
from django.shortcuts import render,redirect
from app.projects.serializers import ProjectSerializer
from app.projects.models import Projects
from app.users.models import UserProfile
from datetime import datetime, timedelta



## written by aarti
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
			return Response("Error")

	# def get(self,request,id=None):
	# 	# import pdb;pdb.set_trace();
	# 	# if(id):
	# 	# 	task_data = Tasks.objects.get(pk=id)
	# 	# 	user_tasks = TaskSerializer(task_data)
	# 	# else:
	# 	task_data = Tasks.objects.all()
	# 	user_tasks = TaskSerializer(task_data,many=True)
	# 	return render(request,'datewise_all_details.html',user_tasks.data)
	# 	# return Response(user_data.data,status=status.HTTP_200_OK)
	
	# def put(self,request,id):
	# 	try:
	# 		get_data = Tasks.objects.get(pk=id)
	# 		update_data = TaskSerializer(get_data,data=request.data)
	# 		if update_data.is_valid():
	# 			update_data.save()
	# 			return Response(update_data.data,status=status.HTTP_200_OK)
	# 	except:
	# 		return Response("Error")


class EditTask(APIView):
	def get(self,request,user_id=None):
		try:
			# import pdb;pdb.set_trace();
			id_list = []
			data_list=[]
			if(user_id):
				get_data = Tasks.objects.get(pk=user_id)
				task_data = TaskSerializer(get_data)
				task_dict = task_data.data
				project_id = task_dict['project'].split(',')
				project_ids =list(map(int,project_id))
				get_project_data = Projects.objects.all()
				project_data = ProjectSerializer(get_project_data,many=True)
				date_value = project_data.data
				for index in date_value:
					list_value = index.items()
					dict_data = dict(list_value)
					data_list.append(dict_data['id'])
				for index in project_ids:
					if index in data_list:
						id_list.append(index)
						task_dict['project']=id_list
						user_task_edit = {"usertasks":task_dict}
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
			if user_tasks.is_valid():
				user_tasks.save()
				return Response(user_tasks.data,status=status.HTTP_200_OK)
		except:
			return Response("Error",status=status.HTTP_400_BAD_REQUEST)


## written by aarti
class UserTaskDatewise(APIView):
	def get(self,request,user_id=None):
		usertasks = Tasks.objects.get(pk=user_id)
		user_tasks = TaskSerializer(usertasks)
		return render(request,'datewise_all_details.html',user_tasks.data)

	def post(self,request):
		usertasks = Tasks.objects.all()
		user_tasks = TaskSerializer(usertasks,many=True)
		return Response(user_tasks.data,status=status.HTTP_201_CREATED)


class CalculateHrs(APIView):
	def get(self,request,user_id):
		# get_datas= Tasks.objects.filter(date__year='2018')
		# get_datas= Tasks.objects.filter(date=datetime.date(2018,4,30))
		one_week_ago = datetime.today() - timedelta(days=7)
		get_week_tasks = Tasks.objects.filter(date__gte=one_week_ago,user_id=user_id)
		# get_datas= Tasks.objects.filter(date__range=["2018-04-18", "2018-04-30"],user_id=user_id)
		task_data = TaskSerializer(get_week_tasks,many=True)
		print(task_data.data)
		return Response(task_data.data,status=status.HTTP_201_CREATED)

	def post(self,request,user_id):
		one_month_ago = datetime.today() - timedelta(days=30)
		get_month_tasks = Tasks.objects.filter(date__gte=one_month_ago,user_id=user_id)
		month_data = TaskSerializer(get_month_tasks,many=True)
		return Response(month_data.data,status=status.HTTP_201_CREATED)

