from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import models
from .forms import AdminProfileForm,UpdateProfileForm
from django.forms.models import model_to_dict
# Create your views here.

@login_required
def SeeProfile(request):
	if request.user.is_authenticated():
		if Profile.objects.filter(user=request.user).count() == 0:
			return redirect('fillprofile')
			print("Hello")
		profile_obj = Profile.objects.get(user=request.user)
		u1 = UpdateProfileForm(data=model_to_dict(profile_obj))
		iteru = iter(u1)
		next(iteru)		
	context = {
		'u' : iteru,
	}
	return render(request,"profile.html",context)

@login_required
def UpdateProfile(request):
	profile_obj = Profile.objects.get(user=request.user)
	form = UpdateProfileForm(request.POST or None, instance=profile_obj)
	if form.is_valid():
		form.save()
		return redirect('profile')
		
	context = {
		'form' : form
	}
	return render(request,"updateprofile.html",context)

@login_required
def FillProfile(request):
	form = UpdateProfileForm(request.POST or None, initial={'user': request.user.id})
	print(form)
	if form.is_valid():
		form.save()
		return redirect('profile')
	
	context = {
		'form' : form
	}
	
	return render(request,"updateprofile.html",context)