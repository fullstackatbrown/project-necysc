# Generated by Django 5.1.1 on 2024-10-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necysc_app', '0003_alter_applicant_group_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='allergies_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='initial_for_allergy_treatment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='insurance_provider',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='medication_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='primary_physician_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='primary_physician_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='program',
            field=models.CharField(blank=True, choices=[('D', 'Day'), ('O', 'Overnight'), ('CIT', 'CIT'), ('C', 'Counselor'), ('EA', 'EA')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='signature',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='subscriber_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
