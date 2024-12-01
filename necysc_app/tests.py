from django.test import TestCase
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django import forms
from django.contrib.auth.models import User
from .models import Applicant, GlobalData, ApplicantHealth, POD

class ApplicantModelTestCase(TestCase):
    def setUp(self):
        """Set up an Applicant instance with all required fields populated."""
        self.user = User.objects.create(username="testuser")
        self.applicant = Applicant.objects.create(
            user=self.user,
            applicant_fname="John",
            applicant_lname="Doe",
            applicant_email="john.doe@example.com",
            parent1_fname="Jane",
            parent1_lname="Doe",
            parent1_relationship="M",
            parent1_phone="1234567890",
            parent1_email="jane.doe@example.com",
            parent1_for_POD=True,
            street_address="123 Main St",
            city="Sample City",
            state="Sample State",
            zip_code="12345",
            applicant_bday="2010-01-01",
            applicant_sex="M",
            applicant_grade=5,
            applicant_shirt_size="YM",
            program="ON",
            interest_in_POD_lead=False,
            camp_rule_agreement=True,
            liability_agreement=True,
        )

    def test_applicant_creation(self):
        """Test that an Applicant object is created successfully."""
        self.assertEqual(self.applicant.applicant_fname, "John")
        self.assertEqual(self.applicant.parent1_fname, "Jane")
        self.assertEqual(self.applicant.app_status, "I")  # Default value
        self.assertEqual(self.applicant.health_record_status, "NC")  # Default value
        self.assertTrue(self.applicant.parent1_for_POD)

    def test_applicant_defaults(self):
        """Test that default values are correctly set."""
        self.assertFalse(self.applicant.payment_received)
        self.assertEqual(self.applicant.payment_total, 0)
        self.assertFalse(self.applicant.financial_aid_requested)
        self.assertFalse(self.applicant.interest_in_committee)
        self.assertFalse(self.applicant.listing_on_weekbook)
    
class GlobalDataTestCase(TestCase):
    def setUp(self):
        """Set up the GlobalData singleton with sample values."""
        self.global_data = GlobalData.objects.create(
            day_camp_cost=500.00,
            ON_camp_cost=1000.00,
            EA_camp_cost=750.00,
        )

    def test_global_data_creation(self):
        """Test that GlobalData is created with correct values."""
        self.assertEqual(self.global_data.day_camp_cost, 500.00)
        self.assertEqual(self.global_data.ON_camp_cost, 1000.00)
        self.assertEqual(self.global_data.EA_camp_cost, 750.00)
        self.assertEqual(str(self.global_data), "Global Data Settings")
    
    # make sure we have everything in the init data working and testing, make sure we have access to whatever the models we have and 
    # can still access it
    
    # def test_applicant_creation(self):
    #     """Test that an Applicant object is created successfully."""
    #     self.assertEqual(self.Applicant.applicant_fname, "John")
        # self.assertEqual(self.applicant.applicant_email, "john.doe@example.com")
        # self.assertEqual(self.applicant.parent1_relationship, "M")
        # self.assertEqual(self.applicant.app_status, "I")  # Default value
        # self.assertEqual(self.applicant.health_record_status, "NC")  # Default value

    # def test_health_form_default_values(self):
    #     """Test that health form fields have default values."""
    #     self.assertFalse(self.applicant.health_form_a_received)
    #     self.assertFalse(self.applicant.health_form_b_received)
    #     self.assertFalse(self.applicant.medication_slip_received)

    # def test_applicant_required_fields(self):
    #     """Test that required fields are properly validated."""
    #     with self.assertRaises(Exception):
    #         Applicant.objects.create(
    #             applicant_fname="John",
    #             applicant_lname="Doe",
    #             # Missing required fields like applicant_email
    #         )

    # def test_program_default(self):
    #     """Test the default value for the program field."""
    #     self.assertEqual(self.applicant.program, "ON")


# class GlobalDataTestCase(TestCase):
#     def setUp(self):
#         self.global_data = GlobalData.objects.create(
#             day_camp_cost=500.00,
#             ON_camp_cost=1000.00,
#             EA_camp_cost=750.00,
#         )

#     def test_global_data_creation(self):
#         """Test that the GlobalData singleton is created successfully."""
#         self.assertEqual(self.global_data.day_camp_cost, 500.00)
#         self.assertEqual(str(self.global_data), "Global Data Settings")


# class ProxyModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username="testuser")
#         self.applicant = Applicant.objects.create(
#             user=self.user,
#             applicant_fname="John",
#             applicant_lname="Doe",
#             applicant_email="john.doe@example.com",
#             street_address="123 Main St",
#             city="Sample City",
#             state="Sample State",
#             zip_code="12345",
#             applicant_bday="2010-01-01",
#             applicant_sex="M",
#             applicant_grade=5,
#         )

#     def test_applicant_health_proxy(self):
#         """Test that ApplicantHealth proxy model works correctly."""
#         health_applicant = ApplicantHealth.objects.get(id=self.applicant.id)
#         self.assertIsInstance(health_applicant, ApplicantHealth)
#         self.assertEqual(health_applicant.applicant_fname, "John")

#     def test_pod_proxy(self):
#         """Test that POD proxy model works correctly."""
#         pod_applicant = POD.objects.get(id=self.applicant.id)
#         self.assertIsInstance(pod_applicant, POD)
#         self.assertEqual(pod_applicant.applicant_fname, "John")


# class ApplicantValidationTestCase(TestCase):
#     def test_invalid_applicant_sex_choice(self):
#         """Test that invalid choices for sex raise a validation error."""
#         with self.assertRaises(ValueError):
#             Applicant.objects.create(
#                 applicant_fname="Jane",
#                 applicant_lname="Doe",
#                 applicant_email="jane.doe@example.com",
#                 street_address="456 Elm St",
#                 city="Sample City",
#                 state="Sample State",
#                 zip_code="54321",
#                 applicant_bday="2012-06-15",
#                 applicant_sex="X",  # Invalid choice
#                 applicant_grade=4,
#             )