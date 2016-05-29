from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']

class AdminProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = []