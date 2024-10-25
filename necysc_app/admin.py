from django.contrib import admin
from .models import Applicant
from .models import GlobalData
from solo.admin import SingletonModelAdmin

class ApplicantAdmin(admin.ModelAdmin):
    # allows search by first name or last name
    search_fields = ['applicant_fname', 'applicant_lname']

    # should the time of app refer to the creation time or time last updated?
    list_display =['applicant_fname', 'applicant_lname', 'applicant_bday', 'last_updated_at', 
                   'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 'payment_received', 
                   'health_record_status', 'parent1_fname', 'parent1_lname', 'parent1_email', 'parent1_phone', 
                   'applicant_shirt_size', 'referrals', 'preferred_roommate']

    # filter selector based on year
    list_filter = ['app_year', 'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 'payment_received',
                   'health_record_status', 'applicant_shirt_size', 'referrals', 'preferred_roommate']

# Register your models here.
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(GlobalData, SingletonModelAdmin)

