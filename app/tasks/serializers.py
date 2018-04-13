from rest_framework import serializers
from app.tasks.models import Tasks
from app.projects.models import Projects
from app.projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
	project_details = serializers.SerializerMethodField("getUserProjectsDetail")
	def getUserProjectsDetail(self,obj):
		try:
			return ProjectSerializer(Projects.objects.get(id=obj.project.id)).data
		except Exception as e:
			print(e)
		 
		 
	class Meta:
		model =  Tasks
		fields = ('id','user','project','project_details','billing_hour','non_billing_hour','total_hour','description','is_deleted','created_at','updated_at','status')
		extra_kwargs = {
			'billing': {
				'required':True,
				'error_messages':{

				'required':"Please fill this field",
				}
			}
		}