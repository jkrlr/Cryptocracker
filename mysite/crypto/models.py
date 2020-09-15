from django.contrib.auth.models import User
from django.db import models
from quiz.models import Contests
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll=models.IntegerField()
    phone=models.CharField(max_length=12)
    is_admin=models.BooleanField(blank=True,default=False)
