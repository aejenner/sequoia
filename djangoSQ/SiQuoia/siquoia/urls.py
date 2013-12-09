from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from siquoia import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="siquoia/sq_top.html"), name="sq_top"),
	url(r'^question/', include('question.urls', namespace="question")), 
	url(r'^squser/', include('squser.urls', namespace="squser")), 
    url(r'^ranking/', include('ranking.urls', namespace="ranking")),
    url(r'^admin/', include(admin.site.urls)),

    # Authentication URLs
    url(r'^accounts/login/$', TemplateView.as_view(template_name="siquoia/sq_login.html"), name="sq_login"),
    url(r'^accounts/auth/$', views.sq_auth, name='sq_auth'),
    url(r'^accounts/logout/$', views.sq_logout, name='sq_logout'),
    url(r'^accounts/register/$', views.sq_register, name='sq_register'),

)
