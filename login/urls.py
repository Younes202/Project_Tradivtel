from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView, EmailVerificationSentView, ConfirmEmailView

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('authentication/', views.authentication, name='authentication'),
    path('logout/', views.logout, name='logout'),

]


