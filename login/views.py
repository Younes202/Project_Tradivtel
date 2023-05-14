from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from login.models import users
from login.models import Specialite
from login.models import Technician
from login.models import Equipe


# Create your views here.
def login(request):
    return render(request, 'HTML/LOGIN/authentication.html')


def logout(request):
    return render(request, 'HTML/LOGIN/authentication.html', {'messagelog': 'Log out.'})


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
            return redirect(home)
            # If we get here, none of the users matched the given email and password
    return render(request, 'HTML/LOGIN/authentication.html', {'message': 'Invalid email or password.'})


def home(request):
    return render(request, 'HTML/DASHBOARD/index.html')


def technician(request):
    specialities = Specialite.objects.all()

    speciality_number = Specialite.objects.count()
    technicians = Technician.objects.all()
    technicians_number = Technician.objects.count()

    technician_specialities = technicians.values_list('specialite_id', flat=True)

    context = {'specialities': specialities, 'speciality_number': speciality_number, 'technicians': technicians,
               'technicians_number': technicians_number, 'technician_specialities': technician_specialities,
               }
    return render(request, 'HTML/DASHBOARD/pages/Technicians/technician.html', context)


def tache(request):
    technicians = Technician.objects.all()
    equipes_number = Equipe.objects.count()
    context = {'technicians': technicians, 'equipes_number': equipes_number}
    return render(request, 'HTML/DASHBOARD/pages/Taches/tache.html', context)


def add_special(request):
    if request.method == 'POST':
        specialty_name = request.POST.get('specialtyName')
        specialty_description = request.POST.get('specialtyDescription')
        specialty = {'name': specialty_name, 'description': specialty_description}
        Specialite.objects.create(name=specialty_name, description=specialty_description)
        return redirect('technician')


def add_technician(request):
    if request.method == 'POST':
        fullname = request.POST.get('technician_fullname')
        telephone = request.POST.get('technician_telephone')
        email = request.POST.get('technician_email')
        specialty_id = request.POST.get('specialty_id')
        Technician.objects.create(fullname=fullname, email=email, telephone=telephone, specialite_id=specialty_id)
        return redirect('technician')


def add_equipe(request):
        if request.method == 'POST':
            equipe_name = request.POST['name']
            technician_ids = request.POST.getlist('technicians')
            equipe = Equipe.objects.create(name=equipe_name)
            for technician_id in technician_ids:
                technician = Technician.objects.get(id=technician_id)
                if technician.equipe is None:
                    technician.equipe = equipe
                    technician.save()
            return redirect('tache')

        else:
            technicians = Technician.objects.filter(equipe=None)
        return render(request, 'add_equipe.html', {'technicians': technicians})


def delete_technician(request, technician_id):
    technician = Technician.objects.get(id=technician_id)
    technician.delete()
    return redirect('technician')


def edit_technician(request, technician_id):
    technician = Technician.objects.get(id=technician_id)

    if request.method == 'POST':
        technician.fullname = request.POST.get('fullname')
        technician.email = request.POST.get('email')
        technician.telephone = request.POST.get('telephone')
        technician.specialite_id = request.POST.get('speciality_id')
        technician.save()
        return redirect('technician')

    specialities = Specialite.objects.all()
    context = {'technician': technician, 'specialities': specialities}
    return render(request, 'HTML/DASHBOARD/pages/Technicians/edit_technician.html', context)


def test(request):
    specialities = Specialite.objects.all()
    context = {'specialities': specialities}
    a = 'Hello'
    return render(request, 'HTML/DASHBOARD/pages/test.html', {"affi": a})


def delete_speciality(request, speciality_id):
    speciality = Specialite.objects.get(id=speciality_id)
    speciality.delete()
    return redirect('technician')


def edit_speciality(request, speciality_id):
    speciality = Specialite.objects.get(id=speciality_id)

    if request.method == 'POST':
        speciality.name = request.POST.get('name')
        speciality.description = request.POST.get('description')
        speciality.save()
        return redirect('technician')
    context = {'speciality': speciality}
    return render(request, 'HTML/DASHBOARD/pages/Technicians/edit_speciality.html', context)
