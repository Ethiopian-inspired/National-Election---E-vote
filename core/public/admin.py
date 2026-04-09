from django.contrib import admin
from .models import (
    Comptition_Request_model,
    Approvement_Token,
    Vote
)
# Register your models here.

admin.site.register (Comptition_Request_model),
admin.site.register (Approvement_Token),
admin.site.register (Vote)