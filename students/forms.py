from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    name = forms.CharField(help_text='Required')
    rollno = forms.CharField(help_text='Required')
    phonenumber = forms.IntegerField(help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'name', 'rollno', 'phonenumber', 'password1', 'password2')

def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["extra_field"]
        if commit:
            user.save()
        return user
