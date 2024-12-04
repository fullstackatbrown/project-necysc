from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Applicant

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateAuthenticationForm(AuthenticationForm):    
    class Meta:
        model = User
        fields = ['username', 'password']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [# camper info
                  'applicant_fname', 'applicant_lname', 'applicant_chinese_name', 'applicant_email',
                  'applicant_bday', 'applicant_sex', 'applicant_grade', 'applicant_shirt_size', 
                  'program', 
                  'street_address', 'city', 'state', 'zip_code',

                  # parent/guardian/emergency contact info
                  'parent1_fname', 'parent1_lname', 'parent1_relationship', 'parent1_phone', 'parent1_email', 'parent1_for_POD',
                  'parent2_fname', 'parent2_lname', 'parent2_relationship', 'parent2_phone', 'parent2_email', 'parent2_for_POD',
                  'additional_emergency_contact_fname', 'additional_emergency_contact_lname', 'additional_emergency_contact_relationship', 'additional_emergency_contact_phone',

                  # POD preference
                  'interest_in_POD_lead',

                  # roommate requests
                  'preferred_roommate',

                  # medical info
                  'insurance_provider', 'subscriber_name', 'primary_physician_name', 'primary_physician_phone',
                  'grant_hospital_permission', 'grant_medical_treatment_permission', 'grant_first_aid_permission', 'grant_meds_permission', 'grant_bug_spray_permission', 'grant_skin_treatment_permission',
                  'allergies', 'allergies_description', 'initial_for_allergy_treatment', 'epi_pen_prescribed',
                  'social_emotional_concerns',
                  'wear_glasses', 'wear_contacts', 'wear_hearing_aids',
                  'medication', 'medication_description', 
                  'opt_out_activities', 'medical_comments',
                  'signature',

                  # pickup info
                  'allowed_pickup_persons', 'available_for_carpool', 

                  # payment info
                  'payment_camp', 'payment_pod', 'payment_donation', 'payment_total', 'financial_aid_requested',
                  
                  # additional info
                  'listing_on_weekbook', 'camper_contact_email', 
                  'interest_in_committee', 'interest_in_wkbook_ads',
                  'referrals', 'heard_from',
                
                  # important docs
                  'camp_rule_agreement', 'liability_agreement',
                  ]
        # Optional fields
    applicant_chinese_name = forms.CharField(
        required=False,
        label="Chinese Name (Optional)"
    )
    parent2_fname = forms.CharField(
        required=False,
        label="Parent 2 First Name (Optional)"
    )
    parent2_lname = forms.CharField(
        required=False,
        label="Parent 2 Last Name (Optional)"
    )
    parent2_relationship = forms.CharField(
        required=False,
        label="Parent 2 Relationship (Optional)"
    )
    parent2_phone = forms.CharField(
        required=False,
        label="Parent 2 Phone (Optional)"
    )
    parent2_email = forms.EmailField(
        required=False,
        label="Parent 2 Email (Optional)"
    )
    allergies = forms.CharField(
        required=False,
        label="Allergies (Optional)",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    preferred_roommate = forms.CharField(
        required=False,
        label="Preferred Roommate (Optional)"
    )
    social_emotional_concerns = forms.CharField(
        required=False,
        label="Social/Emotional Concerns (Optional)"
    )
    wear_glasses = forms.BooleanField(
        required=False,
        label="Wears Glasses (Optional)"
    )
    wear_contacts = forms.BooleanField(
        required=False,
        label="Wears Contacts (Optional)"
    )
    wear_hearing_aids = forms.BooleanField(
        required=False,
        label="Wears Hearing Aids (Optional)"
    )
    medication = forms.BooleanField(
        required=False,
        label="Takes Medication (Optional)"
    )
    medication_description = forms.CharField(
        required=False,
        label="Medication Description (Optional)"
    )
    opt_out_activities = forms.CharField(
        required=False,
        label="Opt-Out Activities (Optional)"
    )
    available_for_carpool = forms.BooleanField(
        required=False,
        label="Available for Carpool (Optional)"
    )
    payment_pod = forms.DecimalField(
        required=False,
        label="POD Waiver Fee (Optional)"
    )
    payment_donation = forms.DecimalField(
        required=False,
        label="Voluntary Donation (Optional)"
    )
    listing_on_weekbook = forms.BooleanField(
        required=False,
        label="Listing on Weekbook (Optional)"
    )
    camper_contact_email = forms.EmailField(
        required=False,
        label="Camper Contact Email (Optional)"
    )
    interest_in_committee = forms.BooleanField(
        required=False,
        label="Interest in Committee (Optional)"
    )
    interest_in_wkbook_ads = forms.BooleanField(
        required=False,
        label="Interest in Weekbook Ads (Optional)"
    )
    referrals = forms.CharField(
        required=False,
        label="Referrals (Optional)"
    )
    heard_from = forms.CharField(
        required=False,
        label="How Did You Hear About Us? (Optional)"
    )

    # Required fields (all others not explicitly listed as optional are required)
    signature = forms.CharField(
        required=True,
        label="Signature",
        help_text="Your signature is required to complete this form.",
    )