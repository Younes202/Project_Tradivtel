from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('authentication/', views.authentication, name='authentication'),
    path('logout/', views.logout, name='logout'),
    path('authentication/home/', views.home, name='home'),
    path('authentication/technician/', views.technician, name='technician'),
    path('authentication/technician/add_special', views.add_special, name='add_special'),
    path('authentication/technician/add_technician', views.add_technician, name='add_technician'),
    path('authentication/technician/delete/<int:technician_id>/', views.delete_technician, name='delete_technician'),
    path('authentication/technician/edit/<int:technician_id>/', views.edit_technician, name='edit_technician'),
    path('authentication/technician/deleteS/<int:speciality_id>/', views.delete_speciality, name='delete_speciality'),
    path('authentication/technician/editS/<int:speciality_id>/', views.edit_speciality, name='edit_speciality'),
    path('test/', views.test, name='test'),

]
