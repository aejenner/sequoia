from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def sq_register_submit(request):
	username = request.POST['username']
	password = request.POST['password']
	password_cnf = request.POST['password_cnf']

	print(username)
	print(password)
	print(password_cnf)

	if password != password_cnf:
		return render(request, 'squser/sq_register.html', {'error_message' : "*Passwords do not match",})

	if username == '' or password == '' or password_cnf == '':
		return render(request, 'squser/sq_register.html', {'error_message' : "*Please fill in all fields",})

	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/question/')
	else:
		return render(request, 'siquoia/sq_register.html', {'error_message' : "Invalid user information",})



