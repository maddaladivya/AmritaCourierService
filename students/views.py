# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from students.models import Profile
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'students/signup.html'
    def get_success_url(self):
        return reverse('profile',kwargs={'pk':self.object.id})


def Profile_view(request,pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        u = Profile.objects.create(user=user, name=name, email=email, phonenumber=phonenumber)
        u.save()
        return HttpResponseRedirect('/students/login')
    return render(request, 'students/profile.html',{})
