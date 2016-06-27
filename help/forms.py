from django import forms
from django.contrib.auth.models import User
from help.models import *

class QueryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['message'] = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = HelpMessage
        exclude = ['reply','messageDateTime','user']
