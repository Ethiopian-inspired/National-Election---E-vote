from django.shortcuts import render, redirect
from .forms import SignUp
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index (request):
    return render (request, 'public/Pages/index.html')

def election (request):
    return render (request, 'public/Pages/SubPages/Election.html')

def signup (request):

    SignForm = SignUp (request.POST or None)

    if request.method == 'POST':
        if SignForm.is_valid():

            username = SignForm.cleaned_data['username']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is Already Taken!!")
                return redirect ('Signup')
            
            SignForm.save()
            messages.success (request, 'Register Valied!')

            return redirect ('Election')
    
    context = {
        'form' : SignForm
    }
    return render (request, 'public/Pages/SubPages/Log/SignUp.html', context=context)