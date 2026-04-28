from django.urls import path
from .views import (
    index,
    election,
    signup,
    logout_request,
    compition_request,
    admin_panel,
    request_approvement,
    approve_page,
    acceptanc_token_page,
    user_token,
    publish_check,
    party_publish,
    vote_page,
    review_vote,
    VoteAPIView
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path ('', index, name='Index'),
    path ('election/', election, name='Election'),
    path ('signup/', signup, name='Signup'),
    path ('logout/', logout_request, name='Logout'),
    path ('compitition_request/', compition_request, name='Compition_Request'),
    path ('admin-panel/<str:username>/', admin_panel, name='Admin_Panel'),
    path ('request-edit/<int:id>', request_approvement, name='Request_Approvement'),
    path ('acceptance_success/<int:id>/', approve_page, name='Acceptanc_token_Page'),
    path ('acceptanc_token_page/<int:id>/', acceptanc_token_page, name='Acceptanc_Token_Page'),
    path ('user_token/<int:id>/', user_token, name='User_Token'),
    path ('published/<int:id>/', publish_check, name="Publish_check"),
    path ('post_party', party_publish, name='Post_party'),
    path ('vote_page/', vote_page, name='Vote_Page'),
    path ('review_vote/<slug:slug>/', review_vote, name='Review_Vote'),
    path ('api/vote/<slug:slug>/', VoteAPIView.as_view(), name="Vote_success"),
    path ('api/token/', TokenObtainPairView.as_view(), name='Token_obtain_pair'),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name='Token_refresh'),


    path (
        'passowrd-reset/',
        auth_views.PasswordResetView.as_view(
            template_name = 'public/Pages/Pass-reset/password-reset.html'
        ),
        name='Password_reset'
    )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)