# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group,GroupManager 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from decorator import group_required
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import TemplateView



class DashboardWelcomeView(TemplateView):
    template_name = 'admin/dashboard/welcome2.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context=context)


def home(request):
    return render(request, 'mysite/home.html')

def auth_dash(request):        
    currentusergroup=request.user.groups.get()
    adming=Group.objects.get(pk=1)            #Group.objects.get(pk=1) = Admin!
    userg=Group.objects.get(pk=2)   
    print request.user.email
    #Group.objects.get(pk=2) = View!
    #print request.user.groups.get()
    #print currentusergroup                                                          #User.objects.get(groups__name)
    if currentusergroup==adming:    
        return redirect('/admin')
    elif currentusergroup==userg:
        return redirect(userdash)

@login_required(redirect_field_name='user_dash')
def userdash(request):
    return render(request, 'mysite/userdash.html')
   # elif User.objects.filter(groups=3):
   #     return render(request, 'mysite/userdash.html')
@login_required(redirect_field_name='admin_dash')
def dash(request):
    return render(request, 'mysite/dash.html')

#@group_required('Admin','View')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})

