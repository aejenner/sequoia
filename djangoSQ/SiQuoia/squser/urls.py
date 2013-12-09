from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from squser import views

urlpatterns = patterns('',
	#url(r'register/$', TemplateView.as_view(template_name="squser/sq_register.html"), name="sq_register"),
	#url(r'register/submit$', views.sq_register_submit, name="sq_register_submit"),
)