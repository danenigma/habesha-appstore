from django.contrib.auth.models import User
from .models import UserProfile,AppProfile
from django import  forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

class AppForm(forms.ModelForm):

	class Meta:
		model = AppProfile
		fields = ('name','catagory','apk','screen_shot','discription')
