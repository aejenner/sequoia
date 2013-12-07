from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from question.models import Question, Category1, Category2, Category3, Choice

# shows the top level category
class C1View(generic.ListView):
	template_name = 'question/c1_list.html'
	context_object_name = 'c1_list'

	def get_queryset(self):
		return Category1.objects.order_by('name')

# shows the 2nd level category contained in the given 1st level category
class C2View(generic.DetailView):
	model = Category1
	template_name = 'question/c2_list.html'
	context_object_name = 'c1'

# shows the 3rd level category contained in the given 2nd level category
class C3View(generic.DetailView):
	model = Category2
	template_name = 'question/c3_list.html'
	context_object_name = 'c2'

class QuestionListView(generic.DetailView):
	model = Category3
	template_name = 'question/question_list.html'
	context_object_name = 'c3'

class AnswerQuestionView(generic.DetailView):
	model = Question
	template_name = 'question/answer_question.html'
	context_object_name = 'q'

def submit(request, c1_pk, c2_pk, c3_pk, q_id):
	q = get_object_or_404(Question, pk=q_id)
	try:
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		q.num_marked_wrong += 1
		q.save()
		return HttpResponse('Wrong!')
	else:
		if selected_choice.is_correct:
			q.num_marked_right += 1
			q.save()
			return HttpResponse('Correct!')
		else:
			q.num_marked_wrong += 1
			q.save()
			return HttpResponse('Wrong!')
