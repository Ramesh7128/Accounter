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


class Project(models.Model):


	projectName = models.CharField(max_length=200, blank=False, null=False)
	projectStartData = models.DateField(blank=False, null=False)
	projectCostPerHr =  models.FloatField(default=0.0)
	projectClient = models.ForeignKey(Client, null=True, blank=True)

	def __unicode__(self):
		if self.projectName:
			return self.projectName
		else:
			return "No Name"
