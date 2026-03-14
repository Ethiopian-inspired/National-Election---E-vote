from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.

# Create profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile (sender, instance, create, **kwargs):
    if create:
        User.objects.create(user=instance)
# ---------------------->

class Profile (models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    # National Id Store inside User Profile
    national_id = models.CharField