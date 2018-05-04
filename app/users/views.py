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
import re
from app.projects.models import Projects
from app.projects.serializers import ProjectSerializer
from app.projects.views import ProjectView
from app.tasks.models import Tasks
from app.tasks.serializers import TaskSerializer
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
import datetime 
import zerosms

## written by aarti
class UserProfileList(APIView):
	
	def post(self,request):
		try:
			user = self.create_user(request)
			if not(user):
				return Response("Error while create user")
			self.overWrite(request, {'user':user.id})
			print(request.data)	
			user_data = UserSerializer(data=request.data)
			if not(user_data.is_valid()):
				return Response(user_data.errors)
			user_data.save()
			return Response(user_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error")

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
				get_name = update_data.data
				current_user_name = get_name['user_name']
				get_username = request.data
				new_user_name = get_username['user_name']
				password = get_username['password']
				confirm_password = get_username['confirm_password']
				if password != '' and confirm_password != '':
					if password == confirm_password:
						user = User.objects.get(username = current_user_name)
						user.set_password(password)
						return Response("PassChanged")
					
				user = User.objects.get(username = current_user_name)
				user.username = new_user_name
				user.save()
				return Response(update_data.data,status=status.HTTP_200_OK)
		except:
			return Response("Error while updating user details")

	def delete(self,request,user_id):
		delete_user=UserProfile.objects.get(pk=user_id)
		delete_user.delete()
		return Response("Deleted",status=status.HTTP_200_OK)

## written by aarti
class Login(TemplateView):
	
	def get(self,request):
		return render(request,'login.html')

	def post(self,request,*args, **kwargs):
		try:
			email = request.POST.get('inputEmail')
			password = request.POST.get('inputPassword')
			if email:
				user = User.objects.get(username=email)
				auth_user = authenticate(username=email, password=password)
				print(auth_user)
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
				return JsonResponse(user_response)

		except Exception as e:
			print(e)
			return JsonResponse({'Error':'err'},status=404)
		
class Dashboard(TemplateView):
	def get(self,request):	
		user_dict = {"test":"yes"}
		return render(request,'employee_dashboard.html',user_dict)
		
	@csrf_exempt
	def post(self,request,user_id=None):
		userData = UserProjects.objects.all()
		user_data = UserProjectSerializer(userData, many=True)
		return JsonResponse({"tt":user_data.data})

class UserDetail(TemplateView):
	def get(self,request):
		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
		data={"uname":user_data.data}
		return render(request,'user_details.html',data)

class AdminDashboard(TemplateView):
	def get(self,request):
		return render(request,'admin_dashboard.html')

class AdminDetails(TemplateView):
	def get(self,request):
		userData = UserProfile.objects.all()
		user_data = UserSerializer(userData, many=True)
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
				project_all = { "projects":project_data.data}
				return JsonResponse(project_all,status=status.HTTP_201_CREATED)
			except Exception as err: 
				print(err) 
				return Response("Error",status=status.HTTP_404_NOT_FOUND)

class WorkDetails(APIView):
	def get(self,request):
		user_info = UserProfile.objects.all()
		user_data = UserSerializer(user_info, many=True)
		user_dict = {"userslist":user_data.data}
		return render(request,'datewise_details.html',user_dict)
	
	##Written By Ashwin
	def post(self,request):
		input_date= request.POST.get("date")
		in_date = input_date.split("-")
		year=int(in_date[0])
		month=int(in_date[1])
		day=int(in_date[2])
		get_tasks= Tasks.objects.filter(date=datetime.date(year,month,day))
		task_data = TaskSerializer(get_tasks,many=True)
		print(task_data.data)
		return Response(task_data.data,status=status.HTTP_201_CREATED)

## written by aarti
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

## written by aarti		
class AssignProjectApi(APIView):
	def post(self,request):
		try:
			project_id = request.POST.get('project')	
			user_id = request.POST.get('user')
			user_data = UserProjectSerializer(data=request.data)
			if not(user_data.is_valid()):
				return Response(user_data.errors)
			user_data.save()
			return Response(user_data.data,status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return JsonResponse({'Error':'error'})

class UserTaskDetails(TemplateView):
	def get(self,request):
		return render(request,'user_task_details.html')

	##Written By Ashwin
class ViewProject(TemplateView):
	def get(self,request):
		return render(request,'viewproject.html')

	def post(self,request):
		try:
			project_Data= Projects.objects.all()
			project_data = ProjectSerializer(project_Data,many=True)
			project_all = { "projects":project_data.data}
			return JsonResponse(project_all,status=status.HTTP_201_CREATED)
		except Exception as err: 
			print(err) 
			return Response("Error",status=status.HTTP_404_NOT_FOUND)

##Written By Ashwin
class SendMail(APIView):
	def get(self,request,user_id):
	    subject = 'Password Changed'
	    get_email = User.objects.get(id = user_id)
	    from_email = 'admin@thoughtwin.com'
	    html_content = "<div><img height='30px' src='https://image.ibb.co/drN81x/1_1.png'><br/><br/><hr><div><h2 style='font-family: Verdana, sans-serif;'>Your Thoughtwin Timesheet password has changed</h2></div><div style='font-family: Verdana, sans-serif;'>Hi "+str(get_email)+",<br><br>We are sending you this notification because your password for Thoughtwin Timesheet has changed.<br><br>If you have not changed it please click below link or button to login again and change your password manually.<br><br><button style='margin: 20px;color: white;background-color: #337AB7;border: 1px;height: 30px;width: 160px; text-decoration:none;font-size: 18px;border-radius: 10px;'><a href='http://127.0.0.1:8000/user/login' target='_blank' style='color: white;text-decoration: none;'> Login</a></button><br><br><a href='http://127.0.0.1:8000/user/login'>http://127.0.0.1:8000/user/login</a> <br><br><br><br>Best Regards<br><br>Thoughtwin team</div></div>"
	    text_content = ""
	    msg = EmailMultiAlternatives(subject,text_content, from_email, [get_email])
	    msg.attach_alternative(html_content, "text/html")
	    msg.send()
	    return HttpResponseRedirect('/user/userprofile')


class SendSms(APIView):
	def get(self,request):
		return render(request,"send_sms.html")

	def post(self,request):
		try:
			username = request.POST.get("username")
			password = request.POST.get("password")
			sendto = request.POST.get("sendto")
			description = request.POST.get("description")
			print(username,password,sendto,description)
			try:
				if username!='' and password !='' and sendto !='' and description!='':
					zerosms.sms(phno=username,passwd=password,receivernum=sendto, message=description)
					return JsonResponse({'send':'send'})
				return JsonResponse({'error':'error'})
			except:
				return JsonResponse({'Error':'error'})
		except Exception as e:
			print(e)
			return JsonResponse({'Error':'error'})
