# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from students.models import Profile, Tickets, Booking
# Register your models here.
admin.site.register(Profile)
admin.site.register(Tickets)
admin.site.register(Booking)
