from django.contrib import admin
from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    # allows search by first name or last name
    search_fields = ['applicant_fname', 'applicant_lname']

    # should the timie of app refer to the creation time or time last updated?
    list_display =['applicant_fname', 'applicant_lname', 'applicant_bday', 'last_updated_at', 
                   'program', 'group_id', 'room_id', 'applicant_sex', 'app_status']

    # filter selector based on year
    list_filter = ['app_year', 'program', 'group_id', 'room_id', 'applicant_sex', 'app_status']

# Register your models here.
admin.site.register(Applicant, ApplicantAdmin)

