from django.conf.urls.defaults import patterns, include, url
from classmanage.manage.views import *

urlpatterns = patterns('',

	url(r'^$', managementdashboards.as_view(), name='dashboard'),
	
	url(r'^createfamily', createfamily.as_view(), name='create_family'),
	url(r'^listfamily', listfamily.as_view(), name='list_family'),
	
	url(r'^family/(?P<pk>\d+)/detail', detailfamily.as_view(), name='detail_family'),
	url(r'^family/(?P<pk>\d+)/createstudent', createstudent.as_view(), name='create_student'),
	url(r'^family/(?P<family_id>\d+)/addstudent', 'classmanage.manage.views.addstudent', name='add_student'),

	url(r'^liststudent', liststudent.as_view(), name='list_student'),
	url(r'^student/(?P<pk>\d+)/detail', detailstudent.as_view(), name='detail_student')
)
