from django.template import Library
from django.contrib.auth.models import User
from accountingapp.models import *

register = Library()


@register.filter
def project_total_hours(projId):
	try:
		project = Project.objects.get(id=projId)
		timeEntry = ProjectTimeEntry.objects.filter(project=project)
		total_time = 0.00
		for time in timeEntry:
			total_time += time.hoursOfWork
		return total_time
	except Exception, e:
		print e
		return 0 

@register.filter
def project_total_cost(projId):
	try:
		project = Project.objects.get(id=projId)
		timeEntry = ProjectTimeEntry.objects.filter(project=project)
		total_time = 0.00
		for time in timeEntry:
			total_time += time.hoursOfWork
		
		total_cost = total_time * project.projectCostPerHr
		return total_cost
	except Exception, e:
		print e
		return 0

@register.filter
def client_total_hours(clientId):
	try:
		client = Client.objects.get(id=clientId)
		clientsProjects = Project.objects.filter(projectClient=client)
		total_client_time = 0
		for project in clientsProjects:
			total_client_time += float(project_total_hours(project.id))
		return total_client_time
	except:
		return 0

@register.filter
def client_total_cost(clientId):
	try:
		client = Client.objects.get(id=clientId)
		clientsProjects = Project.objects.filter(projectClient=client)
		total_client_cost = 0
		for project in clientsProjects:
			total_client_cost += float(project_total_cost(project.id))
		return total_client_cost
	except:
		return 0


# def client_total_cost_per_week(clientId):
# 	try:









