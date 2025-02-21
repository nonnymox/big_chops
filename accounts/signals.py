from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("User Profile Created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create user profile if  it doesnt exist already
            UserProfile.objects.create(user=instance)
            print("User Profile was not present but has been created")
        print("User Profile has been updated")
    


# Using the post_save directly to connect the receiver and sender
# post_save.connect(post_save_create_profile_receiver, sender=User) 