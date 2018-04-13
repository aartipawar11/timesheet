from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from app.projects.models import Projects

class Tasks(models.Model):
	# project = models.ForeignKey(Projects)
	# billing_project = models.ForeignKey('Projects', related_name='billing_project')
	# non_billing_project = models.ForeignKey('Projects', related_name='non_billing_project')
	user = models.ForeignKey(User)
	billing = models.TimeField(auto_now_add=False, blank=True)
	non_billing = models.TimeField(auto_now_add=False, blank=True)
	total = models.TimeField(auto_now_add=False, blank=True)
	billing_description = models.CharField(max_length=1000)
	non_billing_description = models.CharField(max_length=1000)
	date = models.DateField(auto_now_add=False, blank=True)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
