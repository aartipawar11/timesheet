from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects
import datetime

class Tasks(models.Model):
	project = models.CharField(max_length=10)
	user = models.ForeignKey(User)
	billing_hour = models.TimeField(auto_now_add=False, blank=True)
	non_billing_hour = models.TimeField(auto_now_add=False, blank=True)
	total_hour = models.TimeField(auto_now_add=False, blank=True)
	billing_description = models.CharField(max_length=1000,default='Description Not Provided')
	non_billing_description = models.CharField(max_length=1000,default='Description Not Provided')
	date = models.DateField(auto_now_add=False, blank=True,default=datetime.date.today)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)


	# def get_list(self):
	# 	if self.project:
	# 		return self.project.split(',')