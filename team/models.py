from django.db import models
import ast
from events.models import Event
from django.contrib.auth.models import User

# Create your models here.

# class ListField(models.TextField):
#     __metaclass__ = models.SubfieldBase
#     description = "For storing the team members as list"

#     def __init__(self, *args, **kwargs):
#         super(ListField, self).__init__(*args, **kwargs)

#     def to_python(self, value):
#         if not value:
#             value = []

#         if isinstance(value, list):
#             return value

#         return ast.literal_eval(value)

#     def get_prep_value(self, value):
#         if value is None:
#             return value

#         return unicode(value)

#     def value_to_string(self, obj):
#         value = self._get_val_from_obj(obj)
#         return self.get_db_prep_value(value)

class Team(models.Model):
	team_name = models.CharField(max_length=120, unique=True)
	event = models.ForeignKey(Event,max_length=120, related_name = "event_team", on_delete = models.CASCADE)
	team_lead = models.ForeignKey(User, related_name = "team_lead", on_delete = models.CASCADE)
	# team_members = models.ListField()

class Team_Members(models.Model):
	team = models.ForeignKey(Team, related_name = "team",on_delete=models.CASCADE)
	members = models.ForeignKey(User, related_name = "team_members",on_delete=models.CASCADE, blank=True, null=True)
