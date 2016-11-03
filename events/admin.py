from django.contrib import admin
from .models import *

admin.site.register([Event,Indi_Event_Participants,Rounds, Sponsor, FoodFest])
