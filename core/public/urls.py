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
    vote_page
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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