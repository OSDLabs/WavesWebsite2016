from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = []
		widgets = {'user': forms.HiddenInput(),'email': forms.HiddenInput()}

class AdminProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = []

class DisplayProfile(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user', 'pic']