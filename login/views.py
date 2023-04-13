from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'HTML/LOGIN/authentication.html')


def signup(request):
    firstname = request.POST.get('firstName')
    lastname = request.POST.get('lastName')
    email = request.POST.get('email')
    password = request.POST.get('confirmPassword')
    user = {'firstName': firstname, 'lastName': lastname, 'email': email, 'confirmPassword': password}
    return render(request, '/Test.html', user)
