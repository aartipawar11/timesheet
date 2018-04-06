from rest_framework import serializers
from app.users.models import UserProfile,UserProjects
from app.roles.models import Role


class UserSerializer(serializers.ModelSerializer):
	
	role_name = serializers.SerializerMethodField("getRoleDetail")
	def getRoleDetail(self,obj):
		try:
			return Role.objects.get(id=obj.role.id).name
		except Exception as e:
			print(e)
		 
	
	class Meta:
		model = UserProfile
		fields = ('id','user','role','role_name','first_name','last_name','mobile','dob','gender','designation','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'role': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			},
			'first_name': {
				'required':True,
				'error_messages':{
				'required':"first name is required",
				}
			},
			'last_name': {
				'required':True,
				'error_messages':{
				'required':"last name is required"
				}
			},
			'mobile':{
				'required':False,
			},
			'dob':{
				'required':True,
				'error_messages':{
				'required':"dob is required",
				}
			},
			'gender':{
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			},
			'designation':{
				'required':True,
				'error_messages':{
				'required':"fill designation"
				}
			},
			
		}		



