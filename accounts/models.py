from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name or str(self.user)
