# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class staff(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return user.username
