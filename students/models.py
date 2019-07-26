# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False, default='')
    phonenumber = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

class Tickets(models.Model):
    courierid = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    otp = models.IntegerField(max_length=30, default=0)
    status = models.IntegerField(max_length=30, default=0)

    def __str__(self):
        return self.courierid

class Booking(models.Model):
    date = models.DateField()
    s1 = models.IntegerField(default=0)
    s2 = models.IntegerField(default=0)
    s3 = models.IntegerField(default=0)
    s4 = models.IntegerField(default=0)

def __str__(self):
    return self.date
