from django.urls import path
from .views import (
    index,
    election,
    signup,
    logout_request
)

urlpatterns = [
    path ('', index, name='Index'),
    path ('election/', election, name='Election'),
    path ('signup/', signup, name='Signup'),
    path ('logout/', logout_request, name='Logout')
]