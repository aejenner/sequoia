from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^question/', include('question.urls', namespace="question")), 
    url(r'^admin/', include(admin.site.urls)),
)
