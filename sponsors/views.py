from django.shortcuts import render, redirect
from .models import Sponsor, CATEGORY
from django.template import Context
from django.template.defaulttags import register

# Create your views here.

cat_names={}

def sponsors(request):
	cat = []
	for i in CATEGORY:
		cat.append(i[0])
		cat_open = Sponsor.objects.filter(sponsCategory = i[0])
		spons_properties_comb_list = []
		for j in cat_open:
			spons_properties_dict = {}
			spons_properties_dict["names"] = j.sponsName
			spons_properties_dict["pic"] = j.sponsPic
			spons_properties_comb_list.append(spons_properties_dict)
		cat_names[i[0]] = spons_properties_comb_list
	print(cat_names)

	context = {
			"spons_category" : cat,
			"spons_cat" : cat_names
	}

	if request.user.is_authenticated():
		username = request.user.username
		context["username"] = username
	return render(request, "sponsors.html",context)


@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def checkoffset(catlist, catitem):
	if len(catlist)%2 and catlist.index(catitem)==0:
		return True
	else:
		return False

