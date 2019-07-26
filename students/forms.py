from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Tickets


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('courierid', 'user')
