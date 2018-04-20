from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.serializers import TaskSerializer
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from app.tasks.models import Tasks

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

	def get(self,request,id=None):
		# import pdb;pdb.set_trace();
		if(id):
			userprofile = Tasks.objects.get(pk=id)
			user_data = TaskSerializer(userprofile)
		else:
			userData = Tasks.objects.all()
			user_data = TaskSerializer(userData, many=True)
		return Response(user_data.data,status=status.HTTP_200_OK)
	
	# def put(self,request,id):
	# 	try:
	# 		get_data = Tasks.objects.get(pk=id)
	# 		update_data = TaskSerializer(get_data,data=request.data)
	# 		if update_data.is_valid():
	# 			update_data.save()
	# 			return Response(update_data.data,status=status.HTTP_200_OK)
	# 	except:
	# 		return Response("Error")



