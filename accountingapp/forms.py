from django import forms 
import re
from django.contrib.auth.models import User
from accountingapp.models import *
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


class AddClientForm(forms.Form):
    clientName = forms.CharField(label='Client Name', max_length=200)
    clientEmail = forms.EmailField(label='Client Email', max_length=100)
    clientCompany = forms.CharField(label='Client Company', max_length=200)


    def clean_clientEmail(self):
        client_email = self.cleaned_data['clientEmail']
        try:
            Client.objects.get(clientEmail = client_email)
        except ObjectDoesNotExist:
            return client_email
        raise forms.ValidationError('Client with email already exists') 