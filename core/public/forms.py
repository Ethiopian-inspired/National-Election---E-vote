from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUp (UserCreationForm):

    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[50px] border-b-2 border-gray-600/15 focus:border-indigo-600 focus:outline-hidden inter_SemiBold placeholder-gray-400/80',
        'placeholder' : 'Steav'
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