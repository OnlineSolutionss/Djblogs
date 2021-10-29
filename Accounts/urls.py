from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/' , Register , name="register_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),

    path('login/' , Login , name="login"),
    path('dashboard/',Dashboard,name='dashboard'),
    path('logouts/' , Logoutss , name="logouts"),
    
    path('change-password/' , Change_Passwd , name="change_passwd"),

    # Reset Password here
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    # path('password_reset/confirm/<uid64>/token/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html')),

    # #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/confirm/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_complete'),
   
] + static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)
