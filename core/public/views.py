from django.shortcuts import render, redirect
from .forms import (
    SignUp,
    SignIn
)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required (login_url='/signup/')
def index (request):
    return render (request, 'public/Pages/index.html')

def election (request):
    SingInForm = SignIn (request.POST or None)

    if request.method == 'POST':
        if SingInForm.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate (request, username=username, password=password)

            if user is not None:
                login (request, user)
                return redirect ('Index')

    context = {
        'signin' : SingInForm
    }

    return render (request, 'public/Pages/SubPages/Election.html', context=context)

def signup (request):

    SignForm = SignUp (request.POST or None)

    if request.method == 'POST':
        if SignForm.is_valid():
            
            SignForm.save()
            messages.success (request, 'Register Valied!')

            return redirect ('Election')
    
    context = {
        'form' : SignForm
    }
    return render (request, 'public/Pages/SubPages/Log/SignUp.html', context=context)

def logout_request (request):
    logout(request)
    return redirect ('Signup')

def compition_request (request):
    return render (request, 'public/Pages/Comp-page/compition-request-page.html')