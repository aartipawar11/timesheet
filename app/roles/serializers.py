from rest_framework import serializers
from app.users.models import UserProfile
from app.roles.models import Role

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Role
		model = UserProfile
		fields = ('id','name','is_deleted','created_at','updated_at','status')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please insert your role",
				}
			}
		}