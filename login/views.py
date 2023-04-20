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
    return render(request, 'HTML/LOGIN/message_inscription.html', user)


def authentication(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    use = users.objects.all()
    for user in use:
        if user.email == email and user.password == password:
            return render(request, 'HTML/DASHBOARD/index.html')
    # If we get here, none of the users matched the given email and password
    return render(request, 'HTML/LOGIN/authentication.html', {'message': 'Invalid email or password.'})


def logout(request):
    return render(request, 'HTML/LOGIN/authentication.html', {'messagelog': 'Log out.'})
