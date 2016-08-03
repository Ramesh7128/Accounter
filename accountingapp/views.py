from django.shortcuts import render
from accountingapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import Http404
from accountingapp.models import *
from datetime import timedelta
from datetime import date


 
@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)


def register_success(request):
    return render_to_response(
    'success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
 
# @login_required(login_url='/login')
def home(request):
    return render_to_response(
    'accountingapp/home.html',
    { 'user': request.user }
    )

class Clients(View):

	def get(self, request):
		client = Client.objects.filter(user=request.user)
		context = {}
		context['clientlist'] = client
		return render(request, 'accountingapp/clients.html', context)

	def post(self, request):
		if request.POST['action'] == 'delete':
			clientId = self.request.POST['clientid']
			client = Client.objects.get(id=clientId)
			client.delete()
			return HttpResponseRedirect('/clients')
		


class AddClient(View):

	def get(self, request):
		form = AddClientForm()
		context = {}
		context['form'] = form
		return render(request, 'accountingapp/addclient.html',context)

	def post(self, request):
		form =  AddClientForm(request.POST)
		if form.is_valid():
			client = Client()
			client.clientName = form.cleaned_data['clientName']
			client.clientEmail = form.cleaned_data['clientEmail']
			client.clientCompanyInfo = form.cleaned_data['clientCompanyInfo']
			client.user = request.user
			client.save()
			return HttpResponseRedirect('/clients')
		else:
			raise Http404



class Projects(View):

	
	def get(self, request, **kwargs):
		client = Client.objects.get(id=self.kwargs['pk'])
		projectlist = Project.objects.filter(projectClient=client)
		context = {}
		context['projectlist'] = projectlist
		context['client_id'] = self.kwargs['pk']
		return render(request, 'accountingapp/projects.html', context)

	def post(self, request, **kwargs):
		if request.POST['action'] == 'delete':
			projectId = self.request.POST['projectid']
			clientid = self.request.POST['clientid']
			project = Project.objects.get(id=projectId)
			project.delete()
			return HttpResponseRedirect('/clients/'+str(clientid)+'/projects/')



class AddProject(View):

	def get(self, request, **kwargs):

		context = {}
		context['projectClient'] = self.kwargs['pk']
		return render(request, 'accountingapp/addproject.html', context)


	def post(self, request, **kwargs):
		# write checking conditions
		project = Project()
		project.projectName = request.POST.get('projectName')
		project.projectStartDate = request.POST.get('projectStartDate')
		project.projectCostPerHr =  request.POST.get('projectCostPerHr')
		clientId = request.POST.get('projectClient')
		client = Client.objects.get(id=clientId)
		project.projectClient = client
		project.user = request.user
		project.save()
		return HttpResponseRedirect('/clients/'+str(clientId)+'/projects/')



class ProjectTimeList(View):

	def get(self, request, **kwargs):
		proj_id = self.kwargs['pk']
		print proj_id, "kdhnkjsnfkj"
		project = Project.objects.get(id=proj_id)
		try:
			timeEntries = ProjectTimeEntry.objects.filter(project=project)
		except ProjectTimeEntry.DoesNotExist:
			timeEntries = None
		context = {}
		context['timeEntries'] =  timeEntries
		context['projId'] = proj_id
		return render(request, 'accountingapp/project_work_hours.html', context)


	def post(self, request, **kwargs):
		if request.POST['action'] == 'delete':
			proj_id = self.kwargs['pk']
			timeid = self.request.POST['timeid']
			time_entry = ProjectTimeEntry.objects.get(id=timeid)
			time_entry.delete()
			return HttpResponseRedirect('/project/timelist/'+ str(proj_id) + '/')



class AddProjectTime(View):

	def get(self, request, **kwargs):
		context = {}
		context['projectId'] = self.kwargs['pk']
		return render(request, 'accountingapp/add_project_time.html', context)


	def post(self, request, **kwargs):
		projectTime = ProjectTimeEntry()
		projectTime.workDescription = request.POST.get('workDescription')
		projectTime.hoursOfWork = request.POST.get('hoursOfWork')
		projectId = request.POST.get('projectId')
		project = Project.objects.get(id=projectId)
		projectTime.project = project
		projectTime.save()
		return HttpResponseRedirect('/project/timelist/'+ str(projectId) + '/')



class Reports(View):

	def get(self, request, *args, **kwargs):

		user = request.user
		clients = Client.objects.filter(user=user)
		projects = Project.objects.filter(user=user)
		context = {}
		context['clients'] = clients
		context['projects'] = projects
		return render(request, 'accountingapp/summary_reports.html', context)








