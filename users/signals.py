from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#We have a sender and a signal of post_save. 
#So when a user is saved, then send the post_save signal whihc is received by the receiver. 
#Create_profile is run and uses all the entries. 
#Then we create a profile object, with the instance of the user that was created. 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
        
