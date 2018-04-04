from rest_framework.authtoken.models import Token
# from Benemax.app.employment.models import Employment
from app.roles.models import Role
from app.users.models import UserProfile

class RequestOverwrite():

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

	def popParam(self, request, dic):
		print(dic)
		try:
			try:
				if request.data._mutable is False:
					request.data._mutable = True
			except:
				pass
			for key,val in dic.items():
				
				request.data.pop(key)
		except Exception as err:
			print(err)
			return False

class AccessUserObj:

	def fromToken(self, request):
		token = request.META['HTTP_AUTHORIZATION'].replace("Token","")	
		return Token.objects.get(key=str(token).strip())

class AccessRole:
	def fromToken(self, request):
		user = AccessUserObj().fromToken(request).user
		# role,emp = Employment().getRoleForUser(user)
		role = Role().getRole({"id__in":role}).order_by("role_type")
		return role

class AccessRoleType:
	def fromToken(self,request):
		return request.META.get("HTTP_ROLE_TYPE")

class AccessOrg:
	def fromToken(self,request):
		return request.META.get("HTTP_ORG")		

class AccessUserProfile:
	def get(self,request):
		user = AccessUserObj().fromToken(request).user
		return UserProfile().getUserProfile({"user" :  user})

	





					