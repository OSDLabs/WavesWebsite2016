from django.shortcuts import render,redirect
from .models import Event,Indi_Event_Participants, CATEGORY, SPONS, Sponsor, FoodFest
from django.contrib import messages
from django.db.models import Q
from django.template import Context
from django.template.defaulttags import register
from collections import OrderedDict

cat_names = {}

def events(request):
	cat = []
	for i in CATEGORY:
		cat.append(i[0])
		cat_open = Event.objects.filter(event_category = i[0])
		event_props = []
		for j in cat_open:
			event_prop = {}
			event_prop["name"] = j.eventName
			event_prop["date"] = j.eventDate
			event_prop["rules"] = j.eventRules
			event_prop["pic"] = j.eventpic
			event_prop["desc"] = j.event_desc
			event_prop["type"] = j.event_type
			event_props.append(event_prop)
		cat_names[i[0]] = event_props
	# print(cat_names)
	context = {
		"category" : cat,
		"cat":cat_names
	}
	if request.user.is_authenticated():
		username = request.user.username
		context["username"] = username
	return render(request, "front_events.html",context)

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)
@register.filter
def fullf(eventtype):
	return 'Team' if eventtype == 'T' else 'Individual'

@register.filter
def checkoffset(catlist, catitem):
	if len(catlist)%2 and catlist.index(catitem)==0:
		return True
	else:
		return False

def sponsors(request):
	cat = []
	for i in SPONS:
		cat.append(i[0])
		cat_open = Sponsor.objects.filter(spons_type= i[0]).order_by('order')
		event_props = []
		for j in cat_open:
			event_prop = {}
			event_prop["order"] = j.order
			event_prop["desc"] = j.desc
			event_prop["link"] = j.link
			event_prop["img"] = j.img
			event_props.append(event_prop)
		cat_names[i[0]] = event_props
	# print(cat_names)
	context = {
		"category" : cat,
		"cat":cat_names
		}
	return render(request, "front_spons.html",context)

def foodfest(request):
	cat_open = FoodFest.objects.order_by('order')
	event_props = []
	for j in cat_open:
		event_prop = {}
		event_prop["order"] = j.order
		event_prop["desc"] = j.desc
		event_prop["link"] = j.link
		event_prop["img"] = j.img
		event_props.append(event_prop)
	# print(cat_names)
	context = {
		"cat":event_props
		}
	return render(request, "front_food.html",context)


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
	u_reg = Event.objects.filter(event_type = 'T', event__event_part = request.user).order_by('event_category')
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
			return redirect('teamevents')
	except: 
		if request.POST.get('reg'):
			lorem = Indi_Event_Participants(event=u,event_part=request.user)
			lorem.save()
			return redirect('teamevents')

	context = {
		'u': u,
		'reg':reg,
	}

	return render(request,"indeventsreg.html", context)

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