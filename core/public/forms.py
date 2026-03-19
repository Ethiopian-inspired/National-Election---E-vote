from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    Comptition_Request_model
)

from . import models

class SignUp (UserCreationForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]

    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Steve'
    }))

    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Jobs'
    }))

    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Username'
    }))

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Example@gmail.com'
    }))

    password1 = forms.CharField(max_length=10, label='', widget=forms.PasswordInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Password'
    }))

    password2 = forms.CharField(max_length=10, label='', widget=forms.PasswordInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Confirm Password'
    }))

class SignIn (forms.Form):

    username = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Username'
    }))

    password = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Password'
    }))


# Save National Id
class National_ID (forms.ModelForm):

    national_id = forms.CharField (max_length=16, widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'xxxx xxxx xxxx xxxx'
    }))

    class Meta:
        models = User
        fields = ['national_id']
    
    def save(self, commit=True):
        user = super().save(commit=True)

        national_id = self.cleaned_data["national_id"]
        user.profile.national_id = national_id
        user.profile.save()

        return user
    

class Comptition_request (forms.ModelForm):

    class Meta:
        model = Comptition_Request_model
        fields = "__all__"

    party_nik_name = forms.CharField (max_length=5, widget=forms.TextInput(attrs={
        'class' : 'w-full h-[60px] border-none outline-none bg-sky-50 rounded-lg inter_SemiBold placeholder-gray-400/80 pl-6 shadow-sm',
        'placeholder' : 'The Abrivation Of Your Party'
    }))

    party_FullName = forms.CharField (max_length=55, widget=forms.TextInput(attrs={
        'class' : 'w-full h-[60px] border-none outline-none bg-sky-50 rounded-lg inter_SemiBold placeholder-gray-400/80 pl-6 shadow-sm',
        'placeholder' : 'Full Name'
    }))

    party_chairman_name = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'w-full h-[60px] border-none outline-none bg-sky-50 rounded-lg inter_SemiBold placeholder-gray-400/80 pl-6 shadow-sm',
        'placeholder' : 'Party Chair Man Name'
    }))

    want_lead = forms.ChoiceField (choices=[('', 'Select Area')] + models.PLACES_NAME ,widget=forms.Select(attrs={
        'class' : 'w-full h-[60px] border-none outline-none bg-sky-50 rounded-lg inter_SemiBold placeholder-gray-400/80 pl-6 shadow-sm',
        'placeholder' : 'Strict Area To Chooies'
    }))

    party_discription = forms.CharField (widget=forms.Textarea(attrs={
        'class' : 'w-full border-none outline-none bg-sky-50 rounded-lg inter_SemiBold placeholder-gray-400/80 p-6 shadow-sm',
        'placeholder' : 'Discribe Your Party As mach as you can, & idea'
    }))

    party_info_PDF = forms.FileField (widget=forms.ClearableFileInput(attrs={
        'class' : 'hidden shadow-sm'
    }))