from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

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
