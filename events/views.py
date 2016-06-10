from django.shortcuts import render,redirect
from .models import Event,Indi_Event_Participants, CATEGORY
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def Ind_Events(request):
	u_open = Event.objects.filter(event_type = 'S').exclude(event__event_part = request.user).order_by('event_category')
	u_reg = Event.objects.filter(event_type = 'S', event__event_part = request.user).order_by('event_category')
	# If Indi_Event_Participants.objects.filter(event=u,event_part=request.user).count() !=0
	# u2 = Event.objects.filter(event_type = 'S')[0]
	# u1 = Indi_Event_Participants.objects.filter(event__eventName = u2.eventName)
	context = {
		'u': u_open,
		'u1' : u_reg,
	}

	return render(request,"indevents.html", context)

def Team_Events(request):
	u_open = Event.objects.filter(event_type = 'T').exclude(event__event_part = request.user).order_by('event_category')
	u_reg = Event.objects.filter(Q(event_team__team_members = request.user) | Q(event_team__team_lead = request.user), event_type = 'T').order_by('event_category')
	# If Indi_Event_Participants.objects.filter(event=u,event_part=request.user).count() !=0
	# u2 = Event.objects.filter(event_type = 'S')[0]
	# u1 = Indi_Event_Participants.objects.filter(event__eventName = u2.eventName)
	context = {
		'u': u_open,
		'u1' : u_reg,
	}

	return render(request,"teamevents.html", context)

def Team_Events_Reg(request,regid):
	u = Event.objects.get(pk=regid)
	reg = False
	try:
		Indi_Event_Participants.objects.get(event=u,event_part=request.user)
		reg = True
		if request.POST.get('unreg'):
			lorem = Indi_Event_Participants.objects.get(event=u,event_part=request.user)
			lorem.delete()
			return redirect('indevents')
	except: 
		if request.POST.get('reg'):
			lorem = Indi_Event_Participants(event=u,event_part=request.user)
			lorem.save()
			return redirect('indevents')

	context = {
		'u': u,
		'reg':reg,
	}

	return render(request,"teameventsreg.html", context)

def Ind_Events_Reg(request,regid):
	u = Event.objects.get(pk=regid)
	reg = False
	try:
		Indi_Event_Participants.objects.get(event=u,event_part=request.user)
		reg = True
		if request.POST.get('unreg'):
			lorem = Indi_Event_Participants.objects.get(event=u,event_part=request.user)
			lorem.delete()
			return redirect('indevents')
	except: 
		if request.POST.get('reg'):
			lorem = Indi_Event_Participants(event=u,event_part=request.user)
			lorem.save()
			return redirect('indevents')

	context = {
		'u': u,
		'reg':reg,
	}

	return render(request,"indeventsreg.html", context)