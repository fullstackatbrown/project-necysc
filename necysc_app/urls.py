from django.urls import path

from . import views

app_name = "necysc_app"
urlpatterns = [
    # Website Pages
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("programs/", views.programs, name="programs"),
    path("staff/", views.staff, name="staff"),
    path("faq/", views.faq, name="faq"),
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout_view, name="logout"),
    # Applicant Portal Pages
    path("applicant/login/", views.login, name="login"),
    path("applicant/register/", views.register, name="register"),
    path("applicant/", views.home, name="home"),
    path("applicant/new_application/",
         views.new_application, name="new_application"),
    path("applicant/submit_application/",
         views.submit_application, name="submit_application"),
    path("applicant/application_status/",
         views.application_status, name="application_status"),
    path("applicant/application_review/",
         views.application_review, name="application_review"),
    path("applicant/application_review/<int:application_id>/",
         views.application_detail, name="application_detail"),
    path("applicant/edit_application/<int:application_id>/",
         views.edit_application, name="edit_application"),
]
