from email.policy import default
from django.db import models

class Profile(models.Model):
    slackUsername = models.CharField(max_length = 50, null = True)
    age =  models.IntegerField(null=True)
    backend = models.BooleanField(null=True,  default= True)
    bio = models.TextField(null = True)
    


# Create your models here.
