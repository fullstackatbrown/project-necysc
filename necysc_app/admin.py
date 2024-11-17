# admin.py
from django.contrib import admin
from .models import Applicant, ApplicantHealth, GlobalData
from solo.admin import SingletonModelAdmin
from django.http import HttpResponse
import csv

class ApplicantAdmin(admin.ModelAdmin):
    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    download_csv.short_description = "Download selected applications as CSV"
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'last_updated_at', 
                    'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 'payment_received', 
                    'health_record_status', 'parent1_fname', 'parent1_lname', 'parent1_email', 
                    'parent1_phone', 'applicant_shirt_size', 'referrals', 'preferred_roommate']
    list_filter = ['app_year', 'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 
                   'payment_received', 'health_record_status', 'applicant_shirt_size', 'referrals', 
                   'preferred_roommate']
    actions = ["download_csv"]

class HealthInfoAdmin(admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'created_at', 
                    'program', 'applicant_sex', 'health_form_a_received', 'health_form_b_received']

# Register the base model, proxy model, and global data model
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ApplicantHealth, HealthInfoAdmin)
admin.site.register(GlobalData, SingletonModelAdmin)
