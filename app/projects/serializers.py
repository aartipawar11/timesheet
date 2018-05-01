from rest_framework import serializers
from app.projects.models import Projects
from app.users.models import UserProjects

## written by aarti
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



		
