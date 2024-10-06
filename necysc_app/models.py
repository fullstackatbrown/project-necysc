from django.db import models

# Create your models here.
class Applicant(models.Model):
    # APP_STATUS_CHOICES = {
    #     ACCEPTED: "accepted",
    #     DENIED: "denied",
    #     PENDING: "pending",
    #     INCOMPLETE: "incomplete",
    # }

    # general info
    user_email = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)

    # status data
    app_creation_time = models.DateTimeField()
    last_updated = models.DateTimeField()
    app_year = models.IntegerField()
    # app_status = models.CharField(
    #     max_length=200,
    #     choices=APP_STATUS_CHOICES,
    #     # default= # TODO: maybe set a default?
    # )

    pass