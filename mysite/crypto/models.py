from django.contrib.auth.models import User
from django.db import models
# from quiz.models import Contests
# from django.db.models.signals import post_save
# from django.dispatch import receiver  
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    roll_no = models.CharField(max_length=20)
    phone_no=models.CharField(max_length=12)
    is_admin = models.BooleanField(blank=True, default=False)
    
    def __str__(self):
        return str(self.user.username)

 
 
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance) 
 
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

