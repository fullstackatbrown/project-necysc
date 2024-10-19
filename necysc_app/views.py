from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateAuthenticationForm, CreateUserForm

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
    if request.method == 'Post':
        form = CreateAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
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
    context = {}
    return render(request, 'necysc_app/applicant/index.html', context)

def new_application(request):
    context = {}
    return render(request, 'necysc_app/applicant/new_application.html', context)

def application_status(request):
    context = {}
    return render(request, 'necysc_app/applicant/application_status.html', context)

def application_review(request):
    # for reviewing and editing a single application
    context = {}
    return render(request, 'necysc_app/applicant/read_application.html', context)   