# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
import random
from students.models import Tickets, Profile
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
import smtplib
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class home(TemplateView):
    template_name = 'manager/home.html'

def managerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success( request, 'Successful login')
            return HttpResponseRedirect("/manager/home")
    return render(request, 'manager/managerlogin.html', {})

def managerLogout(request):
    logout(request)
    return HttpResponseRedirect("/manager/home")
#   @csrf_exempt

@staff_member_required
def Order(request):
     if request.method == "POST":
         orid = request.POST.get('courierid')
         otp = random.randint(1000,9999)
         status = 0
         try:
             ids = Tickets.objects.get(courierid=orid)
             id = ids.user
             print id
             profile = Profile.objects.get(user = id)
             emailid =  profile.email
             mail = smtplib.SMTP('smtp.gmail.com', 587)
             mail.ehlo()
             mail.starttls()
             mail.login('sarvanimini@gmail.com','sarvani2410')
             mail.sendmail('sarvanimini@gmail.com',emailid, "Your Pin is "+str(otp))
             mail.close()
             u = Tickets.objects.filter(courierid = orid).update(status=1, otp=otp)
             messages.success(request, "Email sent succcessfully!")
         except Tickets.DoesNotExist:
             return HttpResponseRedirect("/manager/addrollno")
     temp = 'manager/courierraisingform.html'
     return render(request,temp,{})

#@csrf_exempt
def addRollNo(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid')
        name = request.POST.get('name')
        otp = random.randint(1000,9999)
        try:
            name = User.objects.get(username = name)
            pro = Profile.objects.get(user = name)
            email = pro.email
            u = Tickets.objects.create(courierid=orderid, user=name, status=1, otp=otp)
            u.save()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('sarvanimini@gmail.com','sarvani2410')
            mail.sendmail('sarvanimini@gmail.com',email,"Your Pin is "+str(otp))
            mail.close()
            messages.success(request, "Email sent succcessfully!")
        except User.DoesNotExist:
            messages.success(request, "Email not sent, check internet connection! or User not registered!")
            return HttpResponseRedirect("/manager/addrollno")
    temp = 'manager/orderidnotfound.html'
    return render(request,temp,{})

#@csrf_exempt
def deliverCourier(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid')
        otp = request.POST.get('otp')
        ord = Tickets.objects.get(courierid = orderid)
        print ord.otp
        print otp
        if str(ord.otp) == str(otp):
            u = Tickets.objects.filter(courierid = ord).update(status=2)
            messages.success(request,"Can deliver!")
        else:
            messages.success(request,"OTP not matched!")
            return HttpResponseRedirect("/manager/deliver")
    temp = 'manager/otpverification.html'
    return render(request,temp,{})
