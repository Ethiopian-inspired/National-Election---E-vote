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
    

class Comptition_request(forms.ModelForm):

    def clean_party_info_PDF(self):
        file = self.cleaned_data.get('party_info_PDF')
        if file and not file.name.lower().endswith('.pdf'):
            raise forms.ValidationError("Only PDF allowed")
        return file
    
    class Meta:
        model = Comptition_Request_model
        fields = "__all__"
        
        widgets = {
            'party_nik_name': forms.TextInput(attrs={
                'class': 'w-full h-[60px] bg-sky-50 rounded-lg pl-6 shadow-sm',
                'placeholder': 'The Abbreviation Of Your Party'
            }),

            'party_FullName': forms.TextInput(attrs={
                'class': 'w-full h-[60px] bg-sky-50 rounded-lg pl-6 shadow-sm',
                'placeholder': 'Full Name'
            }),

            'party_chairman_name': forms.TextInput(attrs={
                'class': 'w-full h-[60px] bg-sky-50 rounded-lg pl-6 shadow-sm',
                'placeholder': 'Party Chairman Name'
            }),

            'want_lead': forms.Select(attrs={
                'class': 'w-full h-[60px] bg-sky-50 rounded-lg pl-6 shadow-sm'
            }),

            'party_discription': forms.Textarea(attrs={
                'class': 'w-full bg-sky-50 rounded-lg p-6 shadow-sm',
                'placeholder': 'Describe your party...'
            }),

            'party_info_PDF': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-sky-50 rounded-lg p-6 shadow-sm'
            }),

            'party_logo': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-sky-50 rounded-lg p-6 shadow-sm'
            }),
        }