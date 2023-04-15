from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView, EmailVerificationSentView, ConfirmEmailView

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("''/email/", EmailVerificationSentView.as_view(), name='account_email_verification_sent'), # vue de confirmation d'envoi de courriel de validation
    path("''/confirm-email/<str:key>/", ConfirmEmailView.as_view(), name='account_confirm_email'), # vue de confirmation d'adresse courriel

]


