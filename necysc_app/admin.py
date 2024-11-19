# admin.py
from django.contrib import admin
from .models import Applicant, ApplicantHealth, GlobalData, CampDirectory, POD, CarpoolApplicant, CamperReferral, RoomateRequest
from solo.admin import SingletonModelAdmin
from django.http import HttpResponse
import csv

class CSVDownloadMixin:
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

    download_csv.short_description = "Download as CSV"
    actions = ["download_csv"]

class ApplicantAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'last_updated_at', 
                    'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 'payment_received', 
                    'health_record_status', 'parent1_fname', 'parent1_lname', 'parent1_email', 
                    'parent1_phone', 'applicant_shirt_size', 'referrals', 'preferred_roommate']
    list_filter = ['app_year', 'program', 'group_id', 'room_id', 'applicant_sex', 'app_status', 
                   'payment_received', 'health_record_status', 'applicant_shirt_size', 'referrals', 
                   'preferred_roommate']

class HealthInfoAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'applicant_bday', 'created_at', 
                    'program', 'applicant_sex', 'health_form_a_received', 'health_form_b_received']

class CampDirectoryAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'street_address', 'applicant_email', 
                    'parent1_email', 'parent1_phone', 'program', 'group_id']
    list_filter = ['program']

class PODAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname','parent1_for_POD', 'parent2_for_POD','parent1_cori_status','parent1_sori_status','parent1_id_status', 'parent2_cori_status','parent2_sori_status','parent2_id_status']

class CarpoolApplicantAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname']
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(available_for_carpool=True)

class CamperReferralAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'referrals']
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(referrals__isnull=True).exclude(referrals__exact='')

class RoomateRequestAdmin(CSVDownloadMixin, admin.ModelAdmin):
    search_fields = ['applicant_fname', 'applicant_lname']
    list_display = ['applicant_fname', 'applicant_lname', 'preferred_roommate']
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(preferred_roommate__isnull=True).exclude(preferred_roommate__exact='')

# Register the base model, proxy model, and global data model
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ApplicantHealth, HealthInfoAdmin)
admin.site.register(GlobalData, SingletonModelAdmin)
admin.site.register(CampDirectory, CampDirectoryAdmin)
admin.site.register(POD, PODAdmin)
admin.site.register(CarpoolApplicant, CarpoolApplicantAdmin)
admin.site.register(CamperReferral, CamperReferralAdmin)
admin.site.register(RoomateRequest, RoomateRequestAdmin)