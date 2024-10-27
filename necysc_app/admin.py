# admin.py
from django.contrib import admin
from .models import Applicant, ApplicantHealth

class ApplicantAdmin(admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'last_updated_at', 
                    'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 'payment_received', 
                    'health_record_status', 'parent1_fname', 'parent1_lname', 'parent1_email', 
                    'parent1_phone', 'applicant_shirt_size', 'referrals', 'preferred_roommate']
    list_filter = ['app_year', 'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 
                   'payment_received', 'health_record_status', 'applicant_shirt_size', 'referrals', 
                   'preferred_roommate']

class HealthInfoAdmin(admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'created_at', 
                    'program', 'applicant_sex', 'health_form_a_received', 'health_form_b_received']

# Register the base model and the proxy model
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ApplicantHealth, HealthInfoAdmin)
