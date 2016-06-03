from django import models
from .models import *
from django.contrib.auth.models import User

# class TeamForm(forms.Form):
# 	def __init__(self, *args, **kwargs):
# 		super(UpdateProfil, self).__init__(*args, **kwargs)
# 		self.fields['institute'] = forms.ModelChoiceField(queryset=Institute.objects)
# 		self.fields['department'] = forms.ModelChoiceField(queryset=Department.objects)

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		exclude = []

class MemberForm(forms.ModelForm):
	class Meta:
		model = Team_Member
		exclude = []

