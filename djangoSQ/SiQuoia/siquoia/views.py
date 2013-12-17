from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def sq_auth(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/question/')
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
			return HttpResponseRedirect(reverse('sq_register_success'))
		else:
			args['error_message'] = '*The combination of information you provided can not be used.'
	
	return render_to_response('siquoia/sq_register.html', args, context_instance=RequestContext(request))
