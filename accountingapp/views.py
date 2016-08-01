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
			client.clientCompany = form.cleaned_data['clientCompany']
			client.user = request.user
			client.save()
			return HttpResponseRedirect('/clients')
		else:
			return Http404


class Projects(View):

	# pk = 0

	def get(self, request, **kwargs):
		client = Client.objects.get(id=self.kwargs['pk'])
		projectlist = Project.objects.filter(projectClient=client)
		context = {}
		context['projectlist'] = projectlist
		context['client_id'] = self.kwargs['pk']
		return render(request, 'accountingapp/projects.html', context)



class AddProject(View):

	def get(self, request, **kwargs):

		form = AddProjectForm(initial={'projectClient': self.kwargs['pk']})
		form.fields['projectClient'].widget = forms.HiddenInput()
		context = {}
		context['form'] = form
		return render(request, 'accountingapp/addproject.html', context)


	def post(self, request, **kwargs):
		form  = AddProjectForm(request.POST)
		if form.is_valid():
			project = Project()
			project.projectName = form.cleaned_data['projectName']
			project.projectStartDate = form.cleaned_data['projectStartDate']
			project.projectCostPerHr =  form.cleaned_data['projectCostPerHr']
			clientId = form.cleaned_data['projectClient']
			client = Client.objects.get(id=clientId)
			project.projectClient = client
			project.save()
			return HttpResponseRedirect('/clients/'+str(clientId)+'/projects/')


