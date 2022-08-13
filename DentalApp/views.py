from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from DentalApp.models import Appointment
from DentalApp.forms import AppointmentForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'DentalApp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have successfully registered!')
    return render(request, 'DentalApp/register.html', {'form': form})

def _login(request):
    if request.user.is_authenticated:
            return redirect('/lists')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/lists")
        else:
            messages.info(request, 'Username or Password is incorrect.')
    return render(request, 'DentalApp/login.html')

def _logout(request):
    logout(request)
    return redirect('/login')

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        number = request.POST.get('number', '')
        from_email = request.POST.get('email', '')
        if subject and message and from_email:
            message = f"From: {name}\nPhone Number: {number}\nMessage: {message}"
        try:
            send_mail(subject, message, from_email, ['swapnildalve52@gmail.com'], fail_silently= False)
            messages.info(request, 'Your Message has been sent, we\'ll get back to you soon!')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, 'DentalApp/contact.html')

def services(request):
    return render(request, 'DentalApp/services.html')

def appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your Appointment is successfull!')
    return render(request, 'DentalApp/appointment.html', {'form': form})

@login_required(login_url='/login')
def lists(request):
    appointments = Appointment.objects.all()
    return render(request, 'DentalApp/lists.html',{'appointments': appointments})

def about(request):
    return render(request, 'DentalApp/about.html')

def check(request):
    appointments = Appointment.objects.all().order_by('date','time')
    return render(request, 'DentalApp/check.html',{'appointments': appointments})

@login_required(login_url='/login')
def delete(request, id):
    patient = Appointment.objects.get(id=id)
    patient.delete()
    return redirect('/lists')

@login_required(login_url='/login')
def update(request, id):
    patient = Appointment.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance= patient)
        if form.is_valid():
            form.save()
        return redirect('/lists')
    return render(request, 'DentalApp/update.html', {'patient':patient})