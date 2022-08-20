from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

#Create your forms here.
class UserCreateForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'password1', 'password2')
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields['username'].label = "Username"
		self.fields['email'].label = "Email Address"
		
		
class UserViewForm(forms.ModelForm):
	
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'first_name', 'last_name')


class ProfileUpdateForm(forms.ModelForm):
	# first_name = forms.CharField(max_length=32)
	# last_name = forms.CharField(max_length=32)
	
	class Meta:
		model = Profile
		fields = ('location', 'role', 'level', 'profile_image')

