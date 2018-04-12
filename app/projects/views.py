from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.projects.serializers import ProjectSerializer,UserProjectSerializer
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.projects.models import Projects
from django.contrib.auth.models import User

class ProjectView(APIView):
	
	def post(self,request):
		try:
			project_data = ProjectSerializer(data=request.data)
			if not(project_data.is_valid()):
				return Response(project_data.errors,status=status.HTTP_400_BAD_REQUEST)
			project_data.save()
			return Response(project_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_400_BAD_REQUEST)


	def get(self,request):
		try:
			project_Data= Projects.objects.all()
			project_data = ProjectSerializer(project_Data,many=True)
			return Response(project_data.data)
		except Exception as err: 
			print(err) 
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

	def put(self,request,project_id):
		try:
			
			get_data = Projects.objects.get(pk=project_id)
			update_data = ProjectSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response(update_data.data)
		except:
			return Response("Error")

class UserProjectView(APIView):
	def post(self,request):
		try:
			user = self.create_user(request)
			if not(user):
				return Response("Error while create user",status=status.HTTP_400_BAD_REQUEST)

			self.overWrite(request, {'user':user.id})
			project_data = UserProjectSerializer(data=request.data)
			if not(project_data.is_valid()):
				return Response(project_data.errors,status=status.HTTP_400_BAD_REQUEST)
			project_data.save()
			return Response(project_data.data,status=status.HTTP_201_CREATED)
			print(request.data)	
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


# class AssignProject(TemplateView):
# 	def get(self,request):
# 		project_Data= Projects.objects.all()
# 		project_data = ProjectSerializer(project_Data,many=True)
# 		project_dict={"projectlist":project_data.data}
# 		userData = UserProfile.objects.all()
# 		user_data = UserSerializer(userData, many=True)
# 		user_dict={"userslist":user_data.data}
# 		user_dict.update(project_dict)
# 		# print(user_dict)

# 		return render(request,'assignproject.html',user_dict)

	
