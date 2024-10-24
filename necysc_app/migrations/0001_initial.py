import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_email", models.EmailField(max_length=254)),
                ("user_pw", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated_at", models.DateTimeField(auto_now=True)),
                ("app_year", models.IntegerField(default=2024)),
                (
                    "app_status",
                    models.CharField(
                        choices=[
                            ("A", "Accepted"),
                            ("D", "Denied"),
                            ("P", "Pending"),
                            ("I", "Incomplete"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "health_record_status",
                    models.CharField(
                        choices=[
                            ("NC", "Not checked"),
                            ("FU", "Needs follow up"),
                            ("A", "Approved"),
                        ],
                        default="NC",
                        max_length=2,
                    ),
                ),
                ("applicant_fname", models.CharField(max_length=200)),
                ("applicant_lname", models.CharField(max_length=200)),
                (
                    "applicant_chinese_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("applicant_email", models.EmailField(max_length=254)),
                ("parent1_fname", models.CharField(max_length=200)),
                ("parent1_lname", models.CharField(max_length=200)),
                (
                    "parent1_relationship",
                    models.CharField(
                        choices=[("F", "Father"), ("M", "Mother"), ("G", "Guardian")],
                        max_length=1,
                    ),
                ),
                ("parent1_phone", models.CharField(max_length=15)),
                ("parent1_email", models.EmailField(max_length=254)),
                ("parent1_for_POD", models.BooleanField()),
                (
                    "parent2_fname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "parent2_lname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "parent2_relationship",
                    models.CharField(
                        blank=True,
                        choices=[("F", "Father"), ("M", "Mother"), ("G", "Guardian")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "parent2_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "parent2_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("parent2_for_POD", models.BooleanField(blank=True, null=True)),
                ("interest_in_POD_lead", models.BooleanField()),
                (
                    "additional_emergency_contact_fname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "additional_emergency_contact_lname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "additional_emergency_contact_relationship",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "additional_emergency_contact_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("street_address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("zip_code", models.CharField(max_length=200)),
                ("applicant_bday", models.DateField()),
                (
                    "applicant_sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                (
                    "applicant_grade",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "applicant_shirt_size",
                    models.CharField(
                        choices=[
                            ("YS", "Youth S"),
                            ("YM", "Youth M"),
                            ("YL", "Youth L"),
                            ("AS", "Adult S"),
                            ("AM", "Adult M"),
                            ("AL", "Adult L"),
                            ("AX", "Adult XL"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
