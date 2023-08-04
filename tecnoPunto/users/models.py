from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    cc = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
