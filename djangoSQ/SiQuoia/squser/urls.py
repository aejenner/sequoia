from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
	url(r'^register$', TemplateView.as_view(template_name="squser/sq_register.html"), name="sq_register"),
)