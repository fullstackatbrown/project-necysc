from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Applicant, GlobalData
from .forms import CreateAuthenticationForm, CreateUserForm, ApplicationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

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

def registrationinfo(request):
    context = {}
    return render(request, 'necysc_app/website/registration.html', context)

# Applicant Portal


def login(request):
    # check if user is already logged in
    if request.user.is_authenticated:
        return redirect('necysc_app:home')
    if request.method == 'POST':
        form = CreateAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('necysc_app:home')
    else:
        form = CreateAuthenticationForm()
    context = {'form': form}
    return render(request, 'necysc_app/applicant/login.html', context)


def register(request):
    # check if user is already logged in
    if request.user.is_authenticated:
        return redirect('necysc_app:home')
    
    form = CreateUserForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # fix
            return redirect('necysc_app:login')
    context = {'form': form}
    return render(request, 'necysc_app/applicant/register.html', context)


@login_required
def home(request):
    applications = Applicant.objects.filter(user=request.user)

    context = {'applications': applications}
    return render(request, 'necysc_app/applicant/index.html', context)

# show each application


@login_required
def application_detail(request, application_id):
    application = Applicant.objects.get(id=application_id)
    context = {'application': application}
    if application.user == request.user:
        return render(request, 'necysc_app/applicant/application_detail.html', context)
    else:
        return redirect('necysc_app:home')



@login_required
def edit_application(request, application_id):
    application = Applicant.objects.get(id=application_id, user=request.user)
    if not application.user == request.user:
        return redirect('necysc_app:home')
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('necysc_app:application_detail', application_id=application.id)
    else:
        form = ApplicationForm(instance=application)
    context = {'form': form, 'application': application}
    return render(request, 'necysc_app/applicant/edit_application.html', context)


@login_required
def new_application(request):
    form = ApplicationForm()

    globaldata = GlobalData.get_solo()

    context = {
        "form": form,
        "globaldata": globaldata,
    }
    return render(request, 'necysc_app/applicant/new_application.html', context)


@login_required
def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Create instance but don't save yet
            application = form.save(commit=False)

            # check if application exists
            if not Applicant.objects.filter(user=request.user).exists():
                application.user = request.user        # Assign the current user
                application.save()                     # Now save the instance
               
            form.save()
            return redirect('necysc_app:home')
    else:
        redirect('necysc_app:new_application')
    context = {"form": form}
    return render(request, 'necysc_app/applicant/submit_application.html', context)
