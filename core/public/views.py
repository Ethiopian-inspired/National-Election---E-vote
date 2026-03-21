from django.shortcuts import render, redirect
from .forms import (
    SignUp,
    SignIn,
    Comptition_request
)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import (
    Comptition_Request_model
)

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
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

    form = Comptition_request (request.POST or None, request.FILES or None)

    
    if form.is_valid ():

        form.save()
        messages.success (request, "Your Information is deliverd!!")
        return redirect ('Index')
    context = {
        'Comptition' : form
    }

    return render (request, 'public/Pages/Comp-page/compition-request-page.html', context=context)

def is_admin (user):
    return user.is_staff

@user_passes_test (is_admin)
def admin_panel (request, username):
    Request_display = Comptition_Request_model.objects.all()

    context = {
        'Request_display' : Request_display
    }
    return render (request, 'public/Pages/Admin-request/display-request-info.html', context=context)


def request_approvement (request, id):

    Read = get_object_or_404 (Comptition_Request_model, id=id)

    context = {
        'read' : Read
    }
    return render (request, 'public/Pages/Admin-request/Request-approvement/Request-approvement.html', context=context)