from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects

class Tasks(models.Model):
	project = models.ForeignKey(Projects)
	user = models.ForeignKey(User)
	billing_hour = models.TimeField(auto_now_add=False, blank=True)
	non_billing_hour = models.TimeField(auto_now_add=False, blank=True)
	total_hour = models.TimeField(auto_now_add=False, blank=True)
	description = models.CharField(max_length=500)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
