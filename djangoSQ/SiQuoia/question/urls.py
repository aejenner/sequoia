from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from question import views

urlpatterns = patterns('',
	url(r'^$', login_required(views.C1View.as_view()), name='c1_list'),
	url(r'^(?P<pk>\d+)/$', login_required(views.C2View.as_view()), name='c2_list'),
	url(r'^(?P<c1_pk>\d+)/(?P<pk>\d+)/$', login_required(views.C3View.as_view()), name='c3_list'),
	url(r'^(?P<c1_pk>\d+)/(?P<c2_pk>\d+)/(?P<pk>\d+)/$', login_required(views.QuestionListView.as_view()), name='question_list'),
	url(r'^(?P<c1_pk>\d+)/(?P<c2_pk>\d+)/(?P<c3_pk>\d+)/(?P<pk>\d+)/$', login_required(views.AnswerQuestionView.as_view()), name='answer_question'),
	url(r'(?P<c1_pk>\d+)/(?P<c2_pk>\d+)/(?P<c3_pk>\d+)/(?P<q_id>\d+)/submit$', login_required(views.submit), name='submit'),
)