from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.tasks.serializers import TaskSerializer
from django.contrib.auth.models import User
from django.views.generic import TemplateView

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




# class AssignProject(TemplateView):
# 	def get(self,request):
# 		project_Data = Projects.objects.all()
# 		project_data = ProjectSerializer(project_Data,many=True)
		
# 		project_dict={"projectlist":project_data.data}

# 		userData = UserProfile.objects.all()
# 		user_data = UserSerializer(userData, many=True)
	
# 		user_dict={"userslist":user_data.data}
# 		user_dict.update(project_dict)
		

# 		return render(request,'employee_dashboard.html',user_dict)