from django.shortcuts import render
from django.http import HttpResponse

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
    context = {}
    return render(request, 'necysc_app/applicant/login.html', context)

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