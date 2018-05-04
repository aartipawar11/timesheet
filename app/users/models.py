from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects
from app.roles.models import Role


class UserProfile(models.Model):

	user = models.ForeignKey(User)
	role = models.ForeignKey(Role,default='')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=10,blank=True)
	dob = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	designation = models.CharField(max_length=200)
	model_pic = models.ImageField(upload_to = 'pic_folder/', default ='pic_folder/no-img.jpg')
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'user_profile'

class UserProjects(models.Model):

	user = models.ForeignKey(User)
	project = models.ForeignKey(Projects)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)




































































