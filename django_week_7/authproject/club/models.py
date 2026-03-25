from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_member = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_view_office", "Can access the manager office"),
        ]