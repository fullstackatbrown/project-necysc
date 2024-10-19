from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateAuthenticationForm, CreateUserForm
from .models import Applicant
from django.contrib.auth import login as auth_login, authenticate

# Website Pages
def index(request):
    context = {}
    return render(request, 'necysc_app/website/index.html', context)

def about(request):
    context = {}
    return render(request, 'necysc_app/website/about.html', context)

def programs(request):
    context = {}
    return render(request, 'necysc_app/website/programs.html', context)

def staff(request):
    context = {}
    return render(request, 'necysc_app/website/staff.html', context)

def faq(request):
    context = {}
    return render(request, 'necysc_app/website/faq.html', context)

# Applicant Portal
def login(request):
    if request.method == 'POST':
        form = CreateAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth_login(request, user)
                return redirect('necysc_app:home')
    else:
        form = CreateAuthenticationForm()
    context = {'form': form}
    return render(request, 'necysc_app/applicant/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #fix
            return redirect('necysc_app:login')
    context = {'form': form}
    return render(request, 'necysc_app/applicant/register.html', context)

def home(request):
    if not request.user.is_authenticated:
        return redirect('necysc_app:login')

    applications = Applicant.objects.filter(user=request.user)
    
    context = {'applications': applications}
    return render(request, 'necysc_app/applicant/index.html', context)   

def new_application(request):
    if not request.user.is_authenticated:
        return redirect('necysc_app:login')
    context = {}
    return render(request, 'necysc_app/applicant/new_application.html', context)

def application_status(request):
    if not request.user.is_authenticated:
        return redirect('necysc_app:login')
    context = {}
    return render(request, 'necysc_app/applicant/application_status.html', context)

def application_review(request):
    if not request.user.is_authenticated:
        return redirect('necysc_app:login')
    # for reviewing and editing a single application
    context = {}
    return render(request, 'necysc_app/applicant/read_application.html', context)   