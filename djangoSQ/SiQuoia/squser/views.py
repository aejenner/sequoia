from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

import random

from question.models import Question, Category1, Category2, Category3, Choice
from squser.models import *

def user_top(request):
	return render(request, 'squser/sq_user_top.html');

def sq_start(request):
	return render(request, 'squser/sq_start.html');

def pk_confirm(request, c1_pk=-1, c2_pk=-1, c3_pk=-1):
	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)

	if userInfo.sq_points < 20:
		return render(request, 'squser/sorry.html', {'sq':userInfo.sq_points});

	if c1_pk == -1:
		cName = 'All'
		cType = 'all'
		pk = 0
	elif c2_pk == -1:
		c = Category1.objects.get(pk=c1_pk)
		cName = c.name
		cType = 'c1'
		pk = c.pk
	elif c3_pk == -1:
		c = Category2.objects.get(pk=c2_pk)
		cName = c.name
		cType = 'c2'
		pk = c.pk
	else:
		c = Category3.objects.get(pk=c3_pk)
		cName = c.name
		cType = 'c3'
		pk = c.pk
	

	return render(request, 'squser/pk_confirm.html', {'cName' : cName, 'cType':cType, 'pk':pk ,'sq':userInfo.sq_points});

def pk_get(request):
	cType = request.POST['cType']
	pk = request.POST['pk']
	p = Packet()
	p.save()

	while p.questions.count() < 15:
		p.questions.add(getRandQ(cType, int(pk)))

	p.save()
	t = Completed()
	t.save()

	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)
	userInfo.packet = p
	userInfo.trial = t
	userInfo.save()

	sq = userInfo.sq_points - 20
	userInfo.sq_points = sq
	userInfo.save()

	return render(request, 'squser/pk_success.html');

def getRandQ(cType, pk):
	if cType == 'all':
		return getRandQAll()
	elif cType == 'c1':
		return getRandQC1(pk)
	elif cType == 'c2':
		return getRandQC2(pk)
	else: 
		return getRandQC3(pk)

def getRandQAll():
	c1Set = Category1.objects
	rand_idx = random.randint(0, c1Set.count() - 1)
	rand_c1 = c1Set.all()[rand_idx]
	return getRandQC1(rand_c1.pk)

def getRandQC1(pk):
	c1 = Category1.objects.get(pk=pk)
	c2Set = c1.category2_set
	rand_idx = random.randint(0, c2Set.count() - 1)
	rand_c2 = c2Set.all()[rand_idx]
	return getRandQC2(rand_c2.pk)

def getRandQC2(pk):
	c2 = Category2.objects.get(pk=pk)
	c3Set = c2.category3_set
	rand_idx = random.randint(0, c3Set.count() - 1)
	rand_c3 = c3Set.all()[rand_idx]
	return getRandQC3(rand_c3.pk)

def getRandQC3(pk):
	c3 = Category3.objects.get(pk=pk)
	qSet = c3.question_set
	rand_idx = random.randint(0, qSet.count() - 1)
	return qSet.all()[rand_idx]


def sq_quiz(request):
	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)
	p = userInfo.packet
	
	if p.questions.count() == 0:
		return HttpResponseRedirect('/squser/done')

	q = p.questions.all()[0]
	return render(request, 'squser/sq_quiz.html', {'q':q});


def next(request):

	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)
	p = userInfo.packet
	if p.questions.count() == 0:
		return HttpResponseRedirect('/squser/done')	
	q = p.questions.all()[0]

	correct = False
	try:
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		q.num_marked_wrong += 1
		q.save()
	else:
		if selected_choice.is_correct:
			q.num_marked_right += 1
			q.save()
			correct = True
		else:
			q.num_marked_wrong += 1
			q.save()

	t = Trial(question=q, correct=correct)
	t.save()
	userInfo.trial.trial.add(t)
	p.questions.remove(q)
	p.save()
	userInfo.save()


	return HttpResponseRedirect('/squser/quiz')


def done(request):
	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)
	t = userInfo.trial
	score = 0
	for trial in t.trial.all():
		if trial.correct:
			score = score + 1
	return render(request, 'squser/done.html', {'t':t, 'score':score});


class PkC1(generic.ListView):
	template_name = 'squser/c1_list.html'
	context_object_name = 'c1_list'

	def get_queryset(self):
		return Category1.objects.order_by('name')

class PkC2(generic.DetailView):
	model = Category1
	template_name = 'squser/c2_list.html'
	context_object_name = 'c1'

class PkC3(generic.DetailView):
	model = Category2
	template_name = 'squser/c3_list.html'
	context_object_name = 'c2'


def sq_buy_sq(request):
	user = request.user
	userInfo = SQUserInfo.objects.get(user=user)

	return render(request, 'squser/sq_buy_sq.html', {'sq':userInfo.sq_points});

def buysq(request):
	price = request.POST['total']
	if is_number(price):
		user = request.user
		userInfo = SQUserInfo.objects.get(user=user)
		sq = int(price) + userInfo.sq_points
		userInfo.sq_points = sq
		userInfo.save()
		return render(request, 'squser/thankyou.html');
	else:
		return render(request, 'squser/sq_buy_sq.html', {'error':"Please enter a number without decimal places."});

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
