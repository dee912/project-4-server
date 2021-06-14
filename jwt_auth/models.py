from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    PERSONAL = 'Personal'
    BUSINESS = 'Business'
    account_type = [
        (PERSONAL,  'Personal'),
        (BUSINESS, 'Business'),
    ]

    type = models.CharField(
        max_length=8,
        choices=account_type,
        default=PERSONAL
    )
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=250)
