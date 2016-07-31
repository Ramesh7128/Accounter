from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):

	# User clients model

	clientName = models.CharField(max_length=200, blank=False, null=False)
	clientEmail = models.EmailField(max_length=100, blank=False, null=False)
	clientCompany = models.CharField(max_length=200, blank=False, null=False)
	user = models.ForeignKey(User)

	def __unicode__(self):
		if self.clientName:
			return self.clientName
		else:
			return "No Name"

