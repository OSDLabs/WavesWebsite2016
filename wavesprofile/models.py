from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
import registration

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 120)
	# pic = models.FileField(upload_to = "uploads/")
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	department = models.CharField(max_length = 60)
	gender = models.CharField(max_length = 1)
	dob = models.DateField(auto_now_add = True, auto_now = False)
	year = models.CharField(max_length =2)
	updatedtime = models.DateTimeField(auto_now_add = False, auto_now = True)
	settime = models.DateTimeField(auto_now_add = True, auto_now = False)