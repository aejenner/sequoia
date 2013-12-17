from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from squser.models import *

def sq_top(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/squser/');
	else:	
		return render(request, 'siquoia/sq_top.html')#TemplateView.as_view(template_name="siquoia/sq_top.html")

def sq_auth(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		return render(request, 'siquoia/sq_login.html', {'error_message' : "Invalid user information",})


def sq_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def sq_register(request):
	args = {}
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			user = User.objects.get(username__exact=username)
			packet = Packet()
			packet.save()
			trial = Completed()
			trial.save()
			userInfo = SQUserInfo(user=user, packet=packet, trial=trial, sq_points=20)
			userInfo.save()
			return HttpResponseRedirect(reverse('sq_register_success'))
		else:
			args['error_message'] = '*The combination of information you provided can not be used.'
	
	return render_to_response('siquoia/sq_register.html', args, context_instance=RequestContext(request))
