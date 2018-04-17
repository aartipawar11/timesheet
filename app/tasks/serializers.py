from rest_framework import serializers
from app.tasks.models import Task   
from app.projects.models import Projects

class TaskSerializer(serializers.ModelSerializer):
		 
	class Meta:

		model =  Task
		fields = ('id','user','project','billing','non_billing','total','task_description','is_deleted','created_at','updated_at','status')

		# model =  Tasks
		# fields = ('id','user','project','date','project_details','billing_hour','non_billing_hour','total_hour','billing_description','non_billing_description','is_deleted','created_at','updated_at','status')

		extra_kwargs = {
			'billing': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}