from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^signup/$' , views.register),
	url(r'^login/$' , views.user_login),
	url(r'^home/$' , views.home),
	url(r'^logout/$' , views.user_logout),
	url(r'^dev/$' , views.developer),
	url(r'^dev/upload/$' , views.upload),
	url(r'^top/$' , views.topchart),
	url(r'^new/$' , views.newreleases),
	url(r'^game/$' , views.games),
	url(r'^social/$' , views.social),
	url(r'^down/$' , views.down),
	url(r'^search/$' , views.search),
	url(r'^myapp/$' , views.myapp),
	url(r'^user/$' , views.user_login2),		
	url(r'^educational/$' , views.educational),
	url(r'^(?P<app>[0-9]+)/$', views.down, name='down'),
	url(r'^rating/(?P<app>[0-9]+)/(?P<rate>[0-9]+)/$', views.rating, name='rating'),	
	url(r'^comment/(?P<app>[0-9]+)/$', views.comment, name='comment'),
]

