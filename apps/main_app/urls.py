from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/new$', views.new_user),
	url(r'^session/new$', views.new_session),
	url(r'^session/delete$', views.logout),
	url(r'^session/dashboard$', views.dashboard),	
	url(r'^home$', views.home), 
	url(r'^home/add$', views.add),
	url(r'^process$', views.process),
	url(r'^favorites/(?P<id>\d+)$', views.join),
	url(r'^remove/(?P<id>\d+)$', views.remove),
	url(r'^uploader/(?P<id>\d+)$', views.uploader),
]
