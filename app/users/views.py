from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.users.serializers import UserSerializer,UserProjectSerializer
from app.users.models import UserProfile,UserProjects
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from app.projects.views import ProjectView
from app.projects.serializers import ProjectSerializer
from app.projects.models import Projects
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django import forms

class UserProfileList(APIView):
	
	def post(self,request):
		try:
			
			user = self.create_user(request)
			if not(user):
				return Response("Error while create user",status=status.HTTP_404_NOT_FOUND)

			self.overWrite(request, {'user':user.id})
			print(request.data)	
			user_data = UserSerializer(data=request.data)
			if not(user_data.is_valid()):
				return Response(user_data.errors,status=status.HTTP_404_NOT_FOUND)
			user_data.save()
			return Response(user_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

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
			# user = User.objects.get(user_id =user_id )
			
			
			# 
			
		
		
			
			

			if update_data.is_valid():
				update_data.save()

				# print(update_data.data)
				get_name = update_data.data
				current_user_name = get_name['user_name']
				# print(current_user_name)
				
				# print(request.data)
				get_username = request.data
				new_user_name = get_username['user_name']
				# print(new_user_name)
				password = get_username['password']
				print(password)

				user = User.objects.get(username = current_user_name)
				user.username = new_user_name
				# user.set_password(password)
				user.save()
				

				return Response(update_data.data,status=status.HTTP_200_OK)
		except:
			return Response("Error" ,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,user_id):
		delete_user=UserProfile.objects.get(pk=user_id)
		delete_user.delete()
		return Response("Deleted",status=status.HTTP_200_OK)


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
				print(user_response)

				return JsonResponse(user_response)

		except Exception as e:
			print(e)
			return JsonResponse({'Error':'err'})
		
		
class Dashboard(TemplateView):
	def get(self,request):	
		# user_id=UserProjects.objects.get(pk=user_id)
		user_dict = {"test":"yes"}
		return render(request,'employee_dashboard.html',user_dict)
		# return render(request,'employee_dashboard.html')
	@csrf_exempt
	def post(self,request,user_id=None):
		# idd=request.POST.get('userid')
		# userData = UserProjects.objects.get(user_id=idd)
		userData = UserProjects.objects.all()
		user_data = UserProjectSerializer(userData, many=True)
		# print(user_data.data)
		
		# print(idd)
		print("post !!!!")
		data={
		"hi":"ji"
		}
		return JsonResponse({"tt":user_data.data})
		# return Response(user_data.data,status=status.HTTP_201_CREATED) 

class UserDetail(TemplateView):
	def get(self,request):
		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		# print(user_data.data)
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

class DeleteUser(TemplateView):
	def get(self,request):
		return render(request,'delete_user.html')


class AddProject(TemplateView):
	def get(self,request):
		return render(request,'addproject.html')

class ViewProject(TemplateView):
	def get(self,request):

		return render(request,'viewproject.html')

	def post(self,request):

			try:
				project_Data= Projects.objects.all()
				project_data = ProjectSerializer(project_Data,many=True)
				# print(project_data.data)
				project_all = { "projects":project_data.data}
				
				return JsonResponse(project_all,status=status.HTTP_201_CREATED)
			except Exception as err: 
				print(err) 
				return Response("Error",status=status.HTTP_404_NOT_FOUND)

class WorkDetails(TemplateView):
	def get(self,request):
		user_info = UserProfile.objects.all()
		user_data = UserSerializer(user_info, many=True)
		user_dict = {"userslist":user_data.data}

		user_task=  Tasks.objects.all()
		user_task_id = TaskSerializer(user_task,many=True)
		user_task_dict = {"usertasks":user_task_id.data}
		
		user_task_dict.update(user_dict)
		return render(request,'datewise_details.html',user_task_dict)



	@csrf_exempt	
	def post(self,request):
		try:
			user_list=[]
			data_list = []
			dicti_data = { }
			get_date = request.POST.get('date')
			if get_date:
				new_task = Tasks.objects.all()
				task_data = TaskSerializer(new_task,many=True)
				date_value = task_data.data
				for index in date_value:
					list_value=index.items()
					dict_data = dict(list_value)
					user = dict_data['user']
					date = dict_data['date']
				if date == get_date:
					user_info = UserProfile.objects.all()
					user_data = UserSerializer(user_info, many=True)
					data_dict = user_data.data
					
					for index in data_dict:
						list_value = index.items()
						dict_data = dict(list_value)
						user_id = dict_data['user']
						if user_id in user_list:
							data_list.append(dict_data)
							
				return JsonResponse({"userlist":data_list})
		except Exception as e:
			print(e)
			return JsonResponse({'Error':'error'})



class AssignProject(TemplateView):
	def get(self,request):
		project_Data= Projects.objects.all()
		project_data = ProjectSerializer(project_Data,many=True)
		project_dict={"projectlist":project_data.data}

		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		user_dict={"userslist":user_data.data}
		user_dict.update(project_dict)

		return render(request,'assignproject.html',user_dict)

class AssignProjectApi(APIView):
	

	# @csrf_exempt
	def post(self,request):

		
		
		try:
			
			project_id = request.POST.get('project')	
			user_id = request.POST.get('user')
			print(project_id)
			print(user_id)
				
			user_data = UserProjectSerializer(data=request.data)
			if not(user_data.is_valid()):
				return Response(user_data.errors,status=status.HTTP_404_NOT_FOUND)
			user_data.save()
			return Response(user_data.data,status=status.HTTP_201_CREATED)
			
		except Exception as e:
			print(e)
			return JsonResponse({'Error':'err'})

class UserTaskDetails(TemplateView):
	def get(self,request):
		return render(request,'user_task_details.html')

class UserTaskDatewise(APIView):
	def get(self,request,user_id=None):
		usertasks = Tasks.objects.get(pk=user_id)
		print(usertasks.user)
		user_tasks = TaskSerializer(usertasks)
		return render(request,'datewise_all_details.html',user_tasks.data)
		# return Response(user_tasks.data,status=status.HTTP_200_OK)

# class DateWiseWork(APIView):

# 	def post(self,request):
# 		input_date=request.POST.get('date')
# 		print(input_date)
# 		# objects.all()
# 		# if not 
# 		datewise=Tasks.objects.get(date=input_date)
# 		if datewise:
# 			print("date got!")
# 			# usersall=Tasks.objects.get()
# 		date=TaskSerializer(datewise)
# 		# print(date)
# 		# return Response(input_date,status=status.HTTP_200_OK)
# 		return Response(date.data,status=status.HTTP_200_OK)
# class EditTask(APIView):
# 	def get(self,request,user_id=None):
# 		try:
# 			if(user_id):
# 				userprofilee = Tasks.objects.get(pk=user_id)
# 				user_dataa = TaskSerializer(userprofilee)
# 				usertaskedit = {"usertasks":user_dataa.data}
# 				# return Response(user_dataa.data,status=status.HTTP_200_OK)
# 				return render(request,'edit_each_task.html',usertaskedit)
# 		except:
# 			return Response("Error")
# 		return render(request,'edittask.html')

# 	def post(self,request):
# 		usertasks = Tasks.objects.all()
# 		user_tasks = TaskSerializer(usertasks,many=True)
# 		return Response(user_tasks.data,status=status.HTTP_201_CREATED)

# 	def put(self,request,user_id):
# 		try:
# 			get_data = Tasks.objects.get(pk=user_id)
# 			# print("inside get data")
# 			user_tasks = TaskSerializer(get_data,data=request.data)
# 			print(user_tasks)
# 			if user_tasks.is_valid():
# 				user_tasks.save()
# 				return Response(user_tasks.data,status=status.HTTP_200_OK)
			
# 			# return Response("user_tasks.data")
# 		except:
# 			return Response("Error",status=status.HTTP_400_BAD_REQUEST)
	
	