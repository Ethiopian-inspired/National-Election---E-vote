from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.

# Create profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.utils.text import slugify

import uuid

# Place Name
PLACES_NAME = [
    ('Afar Region', 'Afar Region'),
    ('Amhara Region', 'Amhara Region'),
    ('Benishangul-Gumuz Region', 'Benishangul-Gumuz Region'),
    ('Gambela Region', 'Gambela Region'),
    ('Harari Region', 'Harari Region'),
    ('Oromia Region', 'Oromia Region'),
    ('Somali Region', 'Somali Region'),
    ('Sidama Region', 'Sidama Region'),
    ('South West Ethiopia Peoples Region', 'South West Ethiopia Peoples Region'),
    ('Southern Ethiopia Regional State', 'Southern Ethiopia Regional State'),
    ('Central Ethiopia Regional State', 'Central Ethiopia Regional State'),
    ('Tigray Region', 'Tigray Region')
]
@receiver(post_save, sender=User)
def create_profile (sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# ---------------------->

class Profile (models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    # National Id Store inside User Profile
    national_id = models.CharField

class Comptition_Request_model (models.Model):

# Party Requester

    user = models.ForeignKey (User, on_delete=models.CASCADE, related_name="party_requests")

# Approvment Choice
    PENDING = 'pending'
    APPROVED = 'approved'

# Publish party Info
    PUBLISH = 'publish'
    UNPUBLISH = 'unpublish'

    status = models.CharField (max_length=20, choices=[
        (PENDING, 'pending'),
        (APPROVED, 'approved')
    ],
        default=PENDING
    )

    publish_status = models.CharField (max_length=20, choices=[
        (PUBLISH, 'publish'),
        (UNPUBLISH, 'unpublish')
    ],
        default=UNPUBLISH
    )

    user = models.ForeignKey (User, on_delete=models.CASCADE)

    party_nik_name = models.CharField (max_length=5)
    party_FullName = models.CharField (max_length=55)

    party_chairman_name = models.CharField (max_length=20)

    want_lead = models.CharField (max_length=55 ,choices=PLACES_NAME)

    party_discription = models.TextField ()
    party_info_PDF = models.FileField (upload_to='Parties/PDF/')
    party_logo = models.ImageField (upload_to='Parties_logo/')

    slug = models.SlugField (unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.party_nik_name} (ID:{self.id})"
    
    # ----------------------> converts the party_FullName into a URL-safe slug
    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.party_FullName)
        super().save(*args, **kwargs)
    

class Approvement_Token(models.Model):
    #request_status replace with request
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(
        Comptition_Request_model,
        on_delete=models.CASCADE,
        related_name='tokens'
    )

    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    create_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() >= self.expired_at

    def save(self, *args, **kwargs):
        if not self.expired_at:
            self.expired_at = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)

    def __str__(self):
        return 'ID:_' + str(self.id) + '____|Name:_' + str(self.user) + '____|Party Own:_' + str(self.request)