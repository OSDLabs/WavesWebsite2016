from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HelpMessage(models.Model):
    def __str__(self):
        return self.user.username
    message = models.CharField(max_length=5000, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.CharField(max_length=5000, default="Waiting.......")
    messageDateTime = models.DateTimeField(auto_now_add=True, auto_now=False, null = True)
