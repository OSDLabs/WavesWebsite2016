from django import forms
from .models import *
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UpdateProfileForm, self).__init__(*args, **kwargs)
		# self.fields['institute'] = forms.ModelChoiceField(queryset=Institute.objects)
		# self.fields['department'] = forms.ModelChoiceField(queryset=Department.objects)
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
		exclude = ['user']