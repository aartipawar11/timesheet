from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.roles.serializers import RoleSerializer
from app.roles.models import Role


class RoleView(APIView):
	
	def post(self,request):
		try:
			role_data = RoleSerializer(data=request.data)
			if not(role_data.is_valid()):
				return Response(role_data.errors,status=status.HTTP_404_NOT_FOUND)
			role_data.save()
			return Response(role_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error",status=status.HTTP_404_NOT_FOUND)


	