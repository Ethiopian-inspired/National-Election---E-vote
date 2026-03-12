from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUp (UserCreationForm):

    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold',
        'placeholder' : 'inter_SemiBold text-gray-400'
    }))

    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold',
        'placeholder' : 'inter_SemiBold text-gray-400'
    }))

    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold',
        'placeholder' : 'inter_SemiBold text-gray-400'
    }))

    email = forms.EmailField(max_length=20, label='', widget=forms.EmailInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold',
        'placeholder' : 'inter_SemiBold text-gray-400'
    }))

    password1 = forms.CharField(max_length=10, label='', widget=forms.PasswordInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold'
    }))

    password2 = forms.CharField(max_length=10, label='', widget=forms.PasswordInput(attrs={
        'class' : 'w-full h-[40px] rounded-sm bg-sky-100 pl-2 inter_SemiBold'
    }))