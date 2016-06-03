from django.shortcuts import render
from .forms import *
# Create your views here.

def Team_Form(request):
	if request.method == 'POST':
		form = TeamForm(request.POST)
	else:
		form = TeamForm()
	if form.is_valid():
		form.save()
		

	context = {
		'form' , form,
	}
	return render(request, "teamform.html", context)

def Member_Add(request):
	if request.method = 'POST':
		form = MemberForm(request.POST)
	else:
		form = MemberForm()
	context = {
		'form' : form
	}
	return render(request)