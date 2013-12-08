from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


from question.models import Question, Category1, Category2, Category3

class QRanking(generic.ListView):
	template_name = 'ranking/q_ranking.html'
	context_object_name = 'q_list'

	def get_queryset(self):
		return Question.objects.order_by('easiness')[:50]