from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.serializers import TaskSerializer
from django.contrib.auth.models import User


class TaskView(APIView):
	
	def post(self,request):
		try:
			user = self.create_user(request)
			if not(user):
				return Response("Error while create user",status=status.HTTP_400_BAD_REQUESTD)

			self.overWrite(request, {'user':user.id})
			print(request.data)	
			task_data = TaskSerializer(data=request.data)
			if not(task_data.is_valid()):
				return Response(task_data.errors,status=status.HTTP_400_BAD_REQUEST)
			task_data.save()
			return Response(task_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_400_BAD_REQUEST)

	def overWrite(self, request, dic):
		try:
			try:
				if request.data._mutable is False:
					request.data._mutable = True
			except:
				pass
			for key,value in dic.items():
				request.data[key] = value
		except Exception as err:
			print(err)
			return False

	def create_user(self,request):
		try:
			return User.objects.create_user(username=request.data.get('username'))
		except Exception as err:
			print(err)
			return False		
