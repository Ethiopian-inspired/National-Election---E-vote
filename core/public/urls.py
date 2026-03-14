from django.urls import path
from .views import (
    index,
    election,
    signup,
    logout_request
)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', index, name='Index'),
    path ('election/', election, name='Election'),
    path ('signup/', signup, name='Signup'),
    path ('logout/', logout_request, name='Logout'),

    path (
        'passowrd-reset/',
        auth_views.PasswordResetView.as_view(
            template_name = 'public/Pages/Pass-reset/password-reset.html'
        ),
        name='Password_reset'
    )
]