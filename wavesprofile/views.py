from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import models
from .forms import AdminProfileForm,UpdateProfileForm,DisplayProfile
from django.forms.models import model_to_dict
import registration
from django.contrib.auth.models import User
# Create your views here.

@login_required
def SeeProfile(request):
	if request.user.is_authenticated():
		if Profile.objects.filter(user=request.user).count() == 0:
			return redirect('fillprofile')
			print("Hello")
		profile_obj = Profile.objects.get(user=request.user)
		feeddata = model_to_dict(profile_obj)
		print(feeddata.values)
		u1 = DisplayProfile(data=feeddata)
	context = {
		'obj':profile_obj,
		'u' : u1,
	}
	return render(request,"profile.html",context)

# @login_required
# def UpdateProfile(request):
# 	profile_obj = Profile.objects.get(username=request.user)
# 	form = UpdateProfileForm(request.POST or None, instance=profile_obj)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('profile')
		
# 	context = {
# 		'form' : form
# 	}
# 	return render(request,"updateprofile.html",context)

@login_required
def FillProfile(request):
	if request.method == 'POST':

		if Profile.objects.filter(user=request.user).count() == 0:
			form = UpdateProfileForm(request.POST, request.FILES,initial={'user': request.user.id,'email':User.objects.get(username=request.user.username).email})
		else:
			profile_obj = Profile.objects.get(user=request.user)
			form = UpdateProfileForm(request.POST,request.FILES, instance=profile_obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.email = User.objects.get(username=request.user.username).email
			instance.save()
			return redirect('profile')
	else:
		if Profile.objects.filter(user=request.user).count() == 0:
			form = UpdateProfileForm(initial={'user': request.user.id,'email':User.objects.get(username=request.user.username).email})
		else:
			profile_obj = Profile.objects.get(user=request.user)
			form = UpdateProfileForm(instance=profile_obj)
	context = {
		'form' : form
	}
	
	return render(request,"updateprofile.html",context)

def Dashboard(request):
	return render(request, "dashboard.html")