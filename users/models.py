from django.db import models
from django.contrib.auth.models import AbstractUser
from groups.models import Group


class User(AbstractUser):
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
