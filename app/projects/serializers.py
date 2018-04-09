from rest_framework import serializers
from app.projects.models import Projects
from app.users.models import UserProjects

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Projects 
		fields = ('id','name','description','is_deleted','created_at','updated_at','status')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}


class UserProjectSerializer(serializers.ModelSerializer):
	project_name = serializers.SerializerMethodField("getProjectDetail")
	def getProjectDetail(self,obj):
		try:
			return Projects.objects.get(id=obj.project.id).name
		except Exception as e:
			print(e)
		 
	class Meta:
		model =  Projects 
		fields = ('id','user','project_name','is_deleted','created_at','updated_at','status')
		# extra_kwargs = {
		# 	'name': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"Please fill this field",
		# 		}
		# 	}
		# }