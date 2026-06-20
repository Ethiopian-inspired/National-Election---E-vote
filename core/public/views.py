from django.shortcuts import render, redirect
from .forms import (
    SignUp,
    SignIn,
    Comptition_request
)
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from datetime import timedelta

from .models import (
    Comptition_Request_model,
    Approvement_Token,
    Vote
)

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required (login_url='/signup/')
def index (request):
    if request.user.is_authenticated:
        token = Approvement_Token.objects.filter(user=request.user).first()
    return render (request, 'public/Pages/index.html', { 'token' : token })

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

    if request.method == 'POST':
        form = Comptition_request (request.POST, request.FILES)

        if form.is_valid ():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            
            messages.success (request, "Your Information is deliverd!!")
            return redirect ('Index')
    else:
        form = Comptition_request ()

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


def request_approvement(request, id):

    read = get_object_or_404(Comptition_Request_model, id=id)

    if read.status != "approved":

        context = {
            "read": read
        }
        return render(
            request,
            "public/Pages/Admin-request/Request-approvement/Request-approvement.html",
            context
        )

    else:
        messages.success(request, "The Request Is Already Approved!")
        return redirect("Index")


@staff_member_required
def approve_page (request, id):
    
    approve_token = get_object_or_404 (Comptition_Request_model, id=id)

    if approve_token.status == Comptition_Request_model.APPROVED:

        messages.warning (request, 'This Request is Alreadt Approved!')
        return redirect ('Index')
    
    approve_token.status = Comptition_Request_model.APPROVED
    approve_token.save(update_fields=["status"])
    
    Approvement_Token.objects.create(
        user=approve_token.user,
        request=approve_token,
        expired_at=timezone.now() + timedelta(hours=24)
    )

    messages.success (request, f"'{approve_token.party_nik_name}' request approved and token Generated!")
    return redirect ('Index')
    

def user_token (request, id):

    token = Approvement_Token.objects.filter(
        user=request.user,
        is_used=False
    ).last()

    if request.user == token.user or request.user.is_staff :
        return render (request, 'public/Pages/User Token/UserToken.html', {'token' : token})
    else:
        return redirect ('Index')
    

def publish_check(request, id):

    publish_confirm = get_object_or_404(Comptition_Request_model, id=id)

    if request.method == "POST":
        publish_confirm.publish_status = Comptition_Request_model.PUBLISH
        publish_confirm.save()

        messages.success(request, "Your Party is Published")

    return redirect("Index")

def acceptanc_token_page (request, id):
    approve_token = get_object_or_404 (Comptition_Request_model, id=id)

    if approve_token.status != Comptition_Request_model.APPROVED:
        return HttpResponseForbidden ("The Request Is Not Approved!")
    
    token = Approvement_Token.objects.filter(request=approve_token).order_by('-create_at').first()

    if not token:
        return HttpResponseForbidden ("No Token Found!")

    if request.user != token.user:
        return HttpResponseForbidden ("Not Allowed!!")
    
    if token.is_expired ():
        return HttpResponseForbidden ("The Code Is Expired!!")
    
    if token.is_used:
        return HttpResponseForbidden ("Token is Already Uesd!")
    
    context = {
        'approval_token' : token
    }

    return render (request, 'public/Pages/Admin-request/Request-approvement/token/tokenpage.html', context=context)

@login_required (login_url='/signup/')
def party_publish (request):

    post_status = Comptition_Request_model.objects.filter(
        status = Comptition_Request_model.APPROVED,
        publish_status = Comptition_Request_model.PUBLISH
    )

    context = {
        'data' : post_status
    }

    return render (request, 'public/Pages/Party publish/Party_publish.html', context)

def vote_page (request):

    vote_status = Comptition_Request_model.objects.filter(
        status = Comptition_Request_model.APPROVED,
        publish_status = Comptition_Request_model.PUBLISH
    )

    context = {
        'vote' : vote_status
    }

    return render (request, 'public/Vote/vote.html', context)


def review_vote (request, slug):
    
    User_data = get_object_or_404(Comptition_Request_model, slug=slug)

    context = {
        'user_data' : User_data
    }

    return render (request, 'public/Vote/Review_and_vote/review_and_vote.html', context)


@login_required(login_url='/signup/')
@require_POST
def main_vote_logic(request, slug):

    party = get_object_or_404(Comptition_Request_model, slug=slug)

    # Prevent owner from voting
    if request.user == party.user:
        messages.error(request, "Can't vote your Party!")
        return redirect("Vote_Page")

    # Prevent duplicate vote
    if Vote.objects.filter(user=request.user, party=party).exists():
        messages.error(request, "You're already voted!")
        return redirect("Index")

    # Save vote
    Vote.objects.create(
        user=request.user,
        party=party
    )

    messages.success(request, f"Successfully Voted | {party.party_FullName}")
    return redirect ("Index")