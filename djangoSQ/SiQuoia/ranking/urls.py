from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ranking import views

urlpatterns = patterns('',
	url(r'^$', login_required(views.QRanking.as_view()), name='q_ranking'),
)