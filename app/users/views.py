from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.users.serializers import UserSerializer
from app.users.models import UserProfile
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import re
from app.projects.models import Projects
from app.projects.serializers import ProjectSerializer
from app.projects.views import ProjectView


class UserProfileList(APIView):
	
	def post(self,request):
		try:
			
			user = self.create_user(request)
			if not(user):
				return Response("Error while create user",status=status.HTTP_400_BAD_REQUEST)

			self.overWrite(request, {'user':user.id})
			print(request.data)	
			user_data = UserSerializer(data=request.data)
			if not(user_data.is_valid()):
				return Response(user_data.errors,status=status.HTTP_400_BAD_REQUEST)
			user_data.save()
			return Response(user_data.data,status=status.HTTP_201_CREATED)
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
			return User.objects.create_user(username=request.data.get('email'),email=request.data.get('email'),password=request.data.get('password'))
		except Exception as err:
			print(err)
			return False

	def get(self,request,user_id=None):
		if(user_id):
			userprofile = UserProfile.objects.get(pk=user_id)
			user_data = UserSerializer(userprofile)
		else:
			userData = UserProfile.objects.all()
			user_data = UserSerializer(userData, many=True)
		return Response(user_data.data,status=status.HTTP_200_OK)

	def put(self,request,user_id):
		try:
			get_data = UserProfile.objects.get(pk=user_id)
			update_data = UserSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response(update_data.data,status=status.HTTP_200_OK)
		except:
			return Response("Error" ,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,user_id):
		delete_user=UserProfile.objects.get(pk=user_id)
		delete_user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class Login(TemplateView):
	
	def get(self,request):
		return render(request,'login.html')
	
	# @csrf_exempt
	def post(self,request,*args, **kwargs):

		## written by aarti
		try:
			email = request.POST.get('inputEmail')
			password = request.POST.get('inputPassword')
			if email:
				user = User.objects.get(username=email)
				auth_user = authenticate(username=email, password=password)
				token,created = Token.objects.get_or_create(user_id=user.id)
				print(token)
				if(user):
					userprofile = UserProfile.objects.get(user_id=user.id)
					user_data = UserSerializer(userprofile)
				else:
					userData = UserProfile.objects.all()
					user_data = UserSerializer(userData,many=True)

				token_value = {
					'token':token.key,
					}
				
				user_response = user_data.data
				user_response.update(token_value)
				# print(user_response)
				return JsonResponse(user_response)
		except Exception as e:
			print(e)
			return JsonResponse({'Error':'err'})
		
		
class Dashboard(TemplateView):
	def get(self,request):	
		return render(request,'employee_dashboard.html')

class UserDetail(TemplateView):
	def get(self,request):
		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		print(user_data.data)
		data={"uname":user_data.data}
		return render(request,'user_details.html',data)

class AdminDashboard(TemplateView):
	def get(self,request):
		return render(request,'admin_dashboard.html')

class AdminDetails(TemplateView):
	def get(self,request):
		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		print(user_data.data)
		data={"uname":user_data.data}
		return render(request,'admin_details.html',data)

class AddUser(TemplateView):
	def get(self,request):
		return render(request,'adduser.html')

class AddProject(TemplateView):
	def get(self,request):
		return render(request,'addproject.html')


class WorkDetails(TemplateView):
	def get(self,request):
		return render(request,'datewise_details.html')


class AssignProject(TemplateView):
	def get(self,request):
		project_Data= Projects.objects.all()
		project_data = ProjectSerializer(project_Data,many=True)
		# print(project_data.data)
		project_dict={"projectlist":project_data.data}

		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		# print(user_data.data)
		user_dict={"userslist":user_data.data}
		user_dict.update(project_dict)
		print(user_dict)

		return render(request,'assignproject.html',user_dict)
	# def user_page(request, username):
	# 	try:
	# 		user = User.objects.get(username=username)
	# 	except:
	# 		raise Http404('Requested user not found.')

	# 	template = get_template('assignproject.html')
	# 	variables = Context({
	# 		'username': username,
	# 		 })
	# 	output = template.render(variables)
	# 	return HttpResponse(output)

