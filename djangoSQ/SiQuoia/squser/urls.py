from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from squser import views

urlpatterns = patterns('',
	url(r'^$', login_required(views.user_top), name='sq_user_top'),
	url(r'^start$', login_required(views.sq_start), name='sq_start'),

	# Packet Select
	url(r'^pck$', login_required(views.PkC1.as_view()), name='c1_list'),
	url(r'^pck(?P<pk>\d+)/$', login_required(views.PkC2.as_view()), name='c2_list'),
	url(r'^pck(?P<c1_pk>\d+)/(?P<pk>\d+)/$', login_required(views.PkC3.as_view()), name='c3_list'),

	# Packet Confirm
	url(r'^confirmation$', login_required(views.pk_confirm), name='pk_confirm'),
	url(r'^confirmation(?P<c1_pk>\d+)/$', login_required(views.pk_confirm), name='pk_confirm'),
	url(r'^confirmation(?P<c1_pk>\d+)/(?P<c2_pk>\d+)/$', login_required(views.pk_confirm), name='pk_confirm'),
	url(r'^confirmation(?P<c1_pk>\d+)/(?P<c2_pk>\d+)/(?P<c3_pk>\d+)/$', login_required(views.pk_confirm), name='pk_confirm'),

	url(r'^pk_get$', login_required(views.pk_get), name='pk_get'),

	url(r'^quiz$', login_required(views.sq_quiz), name='sq_quiz'),
	url(r'^next$', login_required(views.next), name='next'),

	url(r'^done$', login_required(views.done), name='done'),


	url(r'^buy$', login_required(views.sq_buy_sq), name='sq_buy_sq'),

	url(r'^buysq$', login_required(views.buysq), name='buysq'),

	#url(r'^success$', login_required(views.pk_success), name='pk_success'),
)