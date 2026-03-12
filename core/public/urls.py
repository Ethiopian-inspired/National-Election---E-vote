from django.urls import path
from .views import index, election, signup

urlpatterns = [
    path ('', index, name='Index'),
    path ('election/', election, name='Election'),
    path ('signup/', signup, name='Signup')
]