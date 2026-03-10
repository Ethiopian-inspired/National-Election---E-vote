from django.urls import path
from .views import index, election

urlpatterns = [
    path ('', index, name='Index'),
    path ('election/', election, name='Election')
]