from django.shortcuts import render
from django.http import HttpResponse
from login.models import users


# Create your views here.
def login(request):
    return render(request, 'HTML/LOGIN/authentication.html')


def signup(request):
    firstname = request.POST.get('firstName')
    lastname = request.POST.get('lastName')
    email = request.POST.get('email')
    password = request.POST.get('confirmPassword')
    user = {'firstName': firstname, 'lastName': lastname, 'email': email, 'confirmPassword': password}
    users.objects.create(first_name=firstname, last_name=lastname, email=email, password=password)
    return render(request, 'Test.html', user)
