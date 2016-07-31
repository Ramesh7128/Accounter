from django.shortcuts import render
from accountingapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
 
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