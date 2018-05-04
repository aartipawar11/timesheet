from rest_framework import serializers
from app.tasks.models import Tasks  
from app.projects.models import Projects
from app.projects.serializers import ProjectSerializer
from django.contrib.auth.models import User
from app.users.models import UserProfile,UserProjects
from app.users.serializers import UserSerializer

## written by aarti
class TaskSerializer(serializers.ModelSerializer):
	project_name = serializers.SerializerMethodField("getProjectDetail")
	def getProjectDetail(self,obj):
		try:
			return Projects.objects.get(id=obj.project.id).name
		except Exception as e:
			print(e)

	
	##Written By Ashwin
	user_name = serializers.SerializerMethodField("getUserName")
	def getUserName(self,obj):
		try:
			return UserProjects.objects.get(id=obj.project.id).id
			# return UserProfile.objects.get(first_name=obj.first_name)
			# return UserSerializer(UserProfile.objects.get(id=obj.project.id)).data
		except Exception as e:
			print(e)
		 
	class Meta:
		model =  Tasks
		fields = ('id','user','user_name','project','date','project_details','billing_hour','non_billing_hour','total_hour','billing_description','non_billing_description','is_deleted','created_at','updated_at','status')
		extra_kwargs = {
				'billing_hour': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}