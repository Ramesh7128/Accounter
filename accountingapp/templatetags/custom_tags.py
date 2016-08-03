from django.template import Library
from django.contrib.auth.models import User
from accountingapp.models import *
from datetime import timedelta
from datetime import date
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

@register.filter
def project_workinghrs_week(projectId):
	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_hours = float(project_total_hours(project.id))
		hrs_per_week = (7.0/days) * (total_hours)
		return hrs_per_week
	except:
		return "NA"


@register.filter
def project_workinghrs_month(projectId):

	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_hours = float(project_total_hours(project.id))
		hrs_per_month = (30.0/days) * (total_hours)
		return hrs_per_month
	except:
		return "NA"

@register.filter
def project_workinghrs_year(projectId):

	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_hours = float(project_total_hours(project.id))
		hrs_per_year = (365.0/days) * (total_hours)
		return hrs_per_year
	except:
		return "NA"


@register.filter
def project_earnings_week(projectId):

	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_earnings = float(project_total_cost(project.id))
		earnings_per_week = (7.0/days) * (total_earnings)
		return earnings_per_week
	except:
		return "NA"

@register.filter
def project_earnings_month(projectId):

	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_earnings = float(project_total_cost(project.id))
		earnings_per_month = (30.0/days) * (total_earnings)
		return earnings_per_month
	except:
		return "NA"


@register.filter
def project_earnings_year(projectId):

	try:
		project = Project.objects.get(id=projectId)
		no_days_elapsed = date.today()-project.projectStartDate
		days = no_days_elapsed.days
		if (days < 0):
			return "NA"
		total_earnings = float(project_total_cost(project.id))
		earnings_per_year = (365.0/days) * (total_earnings)
		return earnings_per_year
	except:
		return "NA"


























