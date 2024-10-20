from django import forms
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator


# TODO: should we make this a forms.ModelForm?
class Applicant(models.Model):
    # choices for application status
    APP_STATUS_CHOICES = {
        "A": "Accepted",
        "D": "Denied",
        "P": "Pending",
        "I": "Incomplete",
    }
    # choices for health record status
    HEALTH_RECORD_STATUS_CHOICES = {
        "NC": "Not checked",
        "FU": "Needs follow up",
        "A": "Approved",
    }
    # choices for parent relationship
    PARENT_RELATIONSHIP_CHOICES = {
        "F": "Father",
        "M": "Mother",
        "G": "Guardian",
    }
    # choices for applicant sex
    SEX_CHOICES = {
        "M": "Male",
        "F": "Female",
        "O": "Other",
    }
    SHIRT_SIZE_CHOICES = {
        "YS": "Youth S",
        "YM": "Youth M",
        "YL": "Youth L",
        "AS": "Adult S",
        "AM": "Adult M",
        "AL": "Adult L",
        "AX": "Adult XL",
    }
    
    # choices for program data
    PROGRAM_CHOICES={
        "D": "Day",
        "ON": "Overnight",
        "CIT": "CIT",
        "C": "Counselor",
        "OPS": "OPS",
        "EA": "EA",
    }

    # choices for forms
    HEALTH_FORM_RECEIVED_CHOICES={
        "NS": "Not Submitted",
        "P": "Pending",
        "A": "Approved",
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # status data
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    app_year = models.IntegerField(default=datetime.datetime.now().year)
    app_status = models.CharField(
        max_length=1,
        choices=APP_STATUS_CHOICES,
         default= "I"
    )
    # this should be hidden from the user
    health_record_status = models.CharField(
        max_length=2,
        choices=HEALTH_RECORD_STATUS_CHOICES,
        default="NC",
    )

    # personal data
    applicant_fname = models.CharField(max_length=200, verbose_name="First Name")
    applicant_lname = models.CharField(max_length=200, verbose_name="Last Name")
    applicant_chinese_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Chinese Name") # optional
    applicant_email = models.EmailField(verbose_name="Email")

    parent1_fname = models.CharField(max_length=200, verbose_name="Primary Contact First Name")
    parent1_lname = models.CharField(max_length=200, verbose_name="Primary Contact Last Name")
    parent1_relationship = models.CharField(
        max_length=1,
        choices=PARENT_RELATIONSHIP_CHOICES,
        verbose_name="Primary Contact Relationship"
    )
    parent1_phone = models.CharField(max_length=15, verbose_name="Primary Contact Phone")
    parent1_email = models.EmailField(verbose_name="Primary Contact Email")
    parent1_for_POD = models.BooleanField(verbose_name="Primary Contact as POD")

    parent2_fname = models.CharField(max_length=200, blank=True, null=True, verbose_name="Secondary Contact First Name") # optional
    parent2_lname = models.CharField(max_length=200, blank=True, null=True, verbose_name="Secondary Contact Last Name") # optional
    parent2_relationship = models.CharField(
        max_length=1,
        choices=PARENT_RELATIONSHIP_CHOICES,
        blank=True, null=True, verbose_name="Secondary Contact Relationship") # optional
    parent2_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Secondary Contact Phone") # optional
    parent2_email = models.EmailField(blank=True, null=True, verbose_name="Secondary Contact Email") # optional
    parent2_for_POD = models.BooleanField(blank=True, null=True, verbose_name="Secondary Contact as POD") # optional

    interest_in_POD_lead = models.BooleanField(verbose_name="Interest in POD Lead")

    additional_emergency_contact_fname = models.CharField(max_length=200, blank=True, null=True, verbose_name="Emergency Contact First Name") # optional
    additional_emergency_contact_lname = models.CharField(max_length=200, blank=True, null=True, verbose_name="Emergency Contact Last Name") # optional
    additional_emergency_contact_relationship = models.CharField(max_length=200, blank=True, null=True, verbose_name="Emergency Contact Relationship") # optional
    additional_emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Emergency Contact Phone") # optional

    street_address = models.CharField(max_length=200, verbose_name="Street")
    city = models.CharField(max_length=200, verbose_name="City")
    state = models.CharField(max_length=200, verbose_name="State")
    zip_code = models.CharField(max_length=200, verbose_name="Zip Code")

    applicant_bday = models.DateField(verbose_name="Birthday")
    applicant_sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        verbose_name="Gender")
    applicant_grade = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="School Grade")
    applicant_shirt_size = models.CharField(
        max_length=2,
        choices=SHIRT_SIZE_CHOICES,
        verbose_name="T-Shirt Size")

    # program data
    program = models.CharField(
        max_length=3,
        choices=PROGRAM_CHOICES,
        default="ON",
        verbose_name="Program"
    )
    payment_received = models.BooleanField(default=False)
    payment_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_camp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_donation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    payment_pod = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    # other
    allowed_pickup_persons = models.CharField(max_length=500, blank=True, null=True)
    financial_aid_requested = models.BooleanField(default=False)
    listing_on_weekbook = models.BooleanField(default=False)
    camper_contact_email = models.EmailField(blank=True, null=True)
    interest_in_committee = models.BooleanField(default=False)
    interest_in_wkbook_ads = models.BooleanField(default=False)
    available_for_carpool = models.BooleanField(default=False)
    referrals = models.CharField(max_length=200, blank=True, null=True)
    heard_from = models.CharField(max_length=200, blank=True, null=True)
    preferred_roommate = models.CharField(max_length=200, blank=True, null=True)

    # forms
    health_form_a_received = models.BooleanField(default=False)
    health_form_b_received = models.BooleanField(default=False)
    medication_slip_received = models.BooleanField(default=False)
    parent1_cori_status = models.CharField(max_length=10, blank=True, null=True)
    parent1_sori_status = models.CharField(max_length=10, blank=True, null=True)
    parent1_id_status = models.CharField(max_length=10, blank=True, null=True)
    parent2_cori_status = models.CharField(max_length=10, blank=True, null=True)
    parent2_sori_status = models.CharField(max_length=10, blank=True, null=True)
    parent2_id_status = models.CharField(max_length=10, blank=True, null=True)
    camper_cori_status = models.CharField(max_length=10, blank=True, null=True)
    camper_sori_status = models.CharField(max_length=10, blank=True, null=True)
    camper_id_status = models.CharField(max_length=10, blank=True, null=True)
    camp_rule_agreement = models.BooleanField(default=False)
    liability_agreement = models.BooleanField(default=False)
    
    # medical data
    insurance_provider = models.CharField(max_length=200, blank=True, null=True, verbose_name="Health Insurance Provider")
    subscriber_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Insurance Subscriber Name")
    primary_physician_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Physician Name")
    primary_physician_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Physician Phone")

    # grant permission to questions - if left false contact guardian(s)
    grant_hospital_permission = models.BooleanField(default=False)
    grant_medical_treatment_permission = models.BooleanField(default=False)
    grant_first_aid_permission = models.BooleanField(default=False)
    grant_meds_permission = models.BooleanField(default=False)
    grant_bug_spray_permission = models.BooleanField(default=False)
    grant_skin_treatment_permission = models.BooleanField(default=False)

    allergies = models.BooleanField(default=False)
    allergies_description = models.CharField(max_length=200, blank=True, null=True)
    initial_for_allergy_treatment = models.CharField(max_length=200, blank=True, null=True)
    epi_pen_prescribed = models.BooleanField(default=False)
    
    social_emotional_concerns = models.CharField(max_length=200, blank=True, null=True)
    
    wear_glasses = models.BooleanField(default=False)
    wear_contacts = models.BooleanField(default=False)
    wear_hearing_aids = models.BooleanField(default=False)

    medication = models.BooleanField(default=False)
    medication_description = models.CharField(max_length=200, blank=True, null=True)

    opt_out_activities = models.CharField(max_length=200, blank=True, null=True)
    medical_comments = models.CharField(max_length=200, blank=True, null=True)

    signature = models.CharField(max_length=200, blank=True, null=True)


    # registration
    
    # TODO: hidden in form
    group_id = models.CharField(max_length=200, blank=True, null=True, default="0")
    room_id = models.CharField(max_length=200, blank=True, null=True)
    internal_comments = models.CharField(max_length=200, blank=True, null=True)
