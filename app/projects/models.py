from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Projects(models.Model):
	name = models.CharField(max_length=500)
	description = models.CharField(max_length=5000)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
