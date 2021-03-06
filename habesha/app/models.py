from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

	user    = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	# Override the __unicode__() method to return out something meaningful!

class AppProfile(models.Model):

	user      =  models.ForeignKey(User)
	name      =  models.CharField(max_length = 100)
	pub_date  =  models.DateField(auto_now_add = True)
	catagory  =  models.CharField(max_length = 100)
	apk       =  models.FileField(upload_to = 'apks',blank = True)
	screen_shot = models.ImageField(upload_to ='screenshots',blank = True)
	down_number = models.IntegerField(default = 0)	
	rating    =  models.FloatField(default  = 0.0)
	rate_no   =  models.IntegerField(default  = 0)
	#comments  =  models.TextField(blank = True)

	discription = models.TextField(blank = True)
	def __str__(self):
        	return self.name
"""
class AppStatus(models.Model):
	#app       =  models.OneToOneField(AppProfile) 
	down_number = models.IntegerField(blank =True)	
	rating    =  models.IntegerField(blank  = True)
"""
class Comment(models.Model):
    app = models.ForeignKey(AppProfile)
    user = models.ForeignKey(UserProfile)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
	return self.text
class UserDownloadHistory(models.Model):
	user    = models.ForeignKey(UserProfile)
	app	= models.ForeignKey(AppProfile)
	down_date  =  models.DateField(auto_now_add = True)
   









