from django.shortcuts import render, redirect
from .forms import SignUp

# Create your views here.

def index (request):
    return render (request, 'public/Pages/index.html')

def election (request):
    return render (request, 'public/Pages/SubPages/Election.html')

def signup (request):

    SignForm = SignUp (request.POST or None)

    if request.method == 'POST':
        if SignForm.is_valid():
            SignForm.save()
            return redirect ('Election')
    
    context = {
        'form' : SignForm
    }
    return render (request, 'public/Pages/SubPages/Log/SignUp.html', context=context)