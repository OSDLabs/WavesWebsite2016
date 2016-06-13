from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
# Create your views here.

# def Team_Form(request):
# 	if request.method == 'POST':
# 		form = TeamForm(request.POST)
# 	else:
# 		form = TeamForm()
# 	if form.is_valid():
# 		form.save()
		

# 	context = {
# 		'form' , form,
# 	}
# 	return render(request, "teamcreate.html", context)

def Team_Create_Event(request,pkid):
	u = Event.objects.get(pk=pkid)
	membersdisabled = True
	if request.method == 'POST':
		form = TeamFormEvent(request.POST, initial = {'team_lead': request.user.id, 'event' : u})
	else:
		form = TeamFormEvent(initial = {'team_lead': request.user.id, 'event' : u})
	print(form.errors)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.event = u
		instance.team_lead = request.user
		instance.save()

	if Team.objects.filter(team_lead = request.user.id, event = u).count() != 0 :
		membersdisabled = False
		form = Team.objects.get(team_lead = request.user.id, event = u)

	if request.GET.get('id'):
		idd = request.GET.get('id')
		Team_Members.objects.get(id=idd, team__event = u).delete()
		return HttpResponseRedirect("events/teamcreate/" + str(u.id))

	members = Team_Members.objects.filter(team__team_lead = request.user, team__event = u)
	if Team.objects.filter(team_lead = request.user.id, event = u).count() > 0:
		form2 = MemberForm(request.POST or None, initial = {'team': Team.objects.get(team_lead = request.user.id, event = u)})
	else:
		form2 = MemberForm(request.POST or None)
	print(form2)
	if form2.is_valid():
		instance = form2.save(commit=False)
		instance.team = Team.objects.get(team_lead = request.user.id, event = u)
		instance.save()

	context = {
		'form': form,
		'dis' : membersdisabled,
		'members': members,
		'form2': form2
	}
	return render(request, "teamcreate.html", context)

def Member_Add(request):
	# if request.method = 'POST':
	# 	form = MemberForm(request.POST)
	# else:
	# 	form = MemberForm()
	# context = {
	# 	'form' : form
	# }
	return render(request)