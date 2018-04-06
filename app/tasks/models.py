from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects

class Task(models.Model):
	project = models.ForeignKey(Projects)
	user = models.ForeignKey(User)
	billing = models.CharField(max_length=2,default="")
	non_billing = models.CharField(max_length=2,default="")
	total = models.CharField(max_length=2,default="")
	task_description = models.CharField(max_length=500)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)