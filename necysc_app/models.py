from django.db import models
import datetime
from django.core.validators import MinValueValidator


# Create your models here.

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
        "O": "Overnight",
        "CIT": "CIT",
        "C": "Counselor",
        "EA": "EA",
    }

    # general info
    user_email = models.EmailField()
    user_pw = models.CharField(max_length=200)

    # status data
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    app_year = models.IntegerField(default=datetime.datetime.now().year)
    app_status = models.CharField(
        max_length=1,
        choices=APP_STATUS_CHOICES,
        # default= # TODO: maybe set a default? pending or incomplete?
    )
    # TODO: this should be hidden from the user
    health_record_status = models.CharField(
        max_length=2,
        choices=HEALTH_RECORD_STATUS_CHOICES,
        default="NC",
        # widget=forms.HiddenInput()
    )

    # personal data
    applicant_fname = models.CharField(max_length=200)
    applicant_lname = models.CharField(max_length=200)
    applicant_chinese_name = models.CharField(max_length=200, blank=True, null=True) # optional
    applicant_email = models.EmailField()

    parent1_fname = models.CharField(max_length=200)
    parent1_lname = models.CharField(max_length=200)
    parent1_relationship = models.CharField(
        max_length=1,
        choices=PARENT_RELATIONSHIP_CHOICES,
    )
    parent1_phone = models.CharField(max_length=15)
    parent1_email = models.EmailField()
    parent1_for_POD = models.BooleanField()

    parent2_fname = models.CharField(max_length=200, blank=True, null=True) # optional
    parent2_lname = models.CharField(max_length=200, blank=True, null=True) # optional
    parent2_relationship = models.CharField(
        max_length=1,
        choices=PARENT_RELATIONSHIP_CHOICES,
        blank=True, null=True) # optional
    parent2_phone = models.CharField(max_length=15, blank=True, null=True) # optional
    parent2_email = models.EmailField(blank=True, null=True) # optional
    parent2_for_POD = models.BooleanField(blank=True, null=True) # optional

    interest_in_POD_lead = models.BooleanField()

    additional_emergency_contact_fname = models.CharField(max_length=200, blank=True, null=True) # optional
    additional_emergency_contact_lname = models.CharField(max_length=200, blank=True, null=True) # optional
    additional_emergency_contact_relationship = models.CharField(max_length=200, blank=True, null=True) # optional
    additional_emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True) # optional

    street_address = models.CharFIeld(max_length=200)
    city = models.CharFIeld(max_length=200)
    state = models.CharFIeld(max_length=200)
    zip_code = models.CharFIeld(max_length=200)

    applicant_bday = models.DateField()
    applicant_sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES)
    applicant_grade = models.IntegerField(validators=[MinValueValidator(0)])
    applicant_shirt_size = models.CharField(
        max_length=2,
        choices=SHIRT_SIZE_CHOICES)

    # program data
    program = models.CharField(
        max_length=3,
        choices=PROGRAM_CHOICES
    )
    payment_received = models.BooleanField(blank=True, null=True)
    # payment_total = models.
    
