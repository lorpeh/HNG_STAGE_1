from email.policy import default
from django.db import models

class Profile(models.Model):
    user_name = models.CharField(max_length = 50, null = True)
    Age =  models.IntegerField(null=True)
    Backend = models.BooleanField(null=True,  default= True)
    Bio = models.TextField(null = True)
    


# Create your models here.
