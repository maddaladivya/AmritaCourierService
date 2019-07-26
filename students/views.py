# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from students.models import Profile, Tickets, Booking
from django.http import HttpResponseRedirect, HttpResponse
from students.forms import TicketForm
from fusioncharts import FusionCharts
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'students/signup.html'
    def get_success_url(self):
        return reverse('profile',kwargs={'pk':self.object.id})
    def form_invalid(self, form):
        messages.success( self.request, 'Check your password')
        return HttpResponseRedirect('/students/signup')


def Profile_view(request,pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        u = Profile.objects.create(user=user, name=name, email=email, phonenumber=phonenumber)
        u.save()
        messages.success(request, 'Registration Successful!')
        return HttpResponseRedirect('/students/login')
    return render(request, 'students/profile.html',{})


class TicketGenerate(generic.CreateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'students/tickets.html'
    def get_success_url(self):
        messages.success(self.request, 'Ticket generated Successfully!')
        return reverse('home')
    def form_invalid(self, form):
        messages.success(self.request, 'Invalid CourierID, already exists!')
        return HttpResponseRedirect('/students/ticket')

class StudentDetails(generic.TemplateView):
    template_name = 'students/details.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(StudentDetails, self).get_context_data(*args, **kwargs)
        ctx['profile'] = Profile.objects.get(user = self.request.user )
        ctx['tickets'] = Tickets.objects.all()
        return ctx

class UpdateDetails(generic.TemplateView):
    template_name = 'students/edit.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(UpdateDetails, self).get_context_data(*args, **kwargs)
        ctx['profile'] = Profile.objects.get(user = self.request.user)
        return ctx

    def post(self, request, *args, **kwargs):
        u = Profile.objects.get(user = self.request.user)
        u.name = request.POST.get('name')
        u.email = request.POST.get('email')
        u.phonenumber = request.POST.get('phonenumber')
        u.save()
        return HttpResponseRedirect('/students/details')

class PublicPage(generic.ListView):
    model = Tickets
    template_name = 'students/publicpage.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(PublicPage, self).get_context_data(*args, **kwargs)
        ctx['tickets'] = Tickets.objects.all()
        return ctx

def book(request):
    if request.method == "POST":
        date = request.POST.get('d')
        slot = request.POST.get('s')
        print date
        try:
            p = Booking.objects.get(date=date)
            if slot == "s1":
                q = p.s1
                q=q+1
                u = Booking.objects.filter(date=date).update(s1=q)
            elif slot == "s2":
                q = p.s2
                q=q+1
                u = Booking.objects.filter(date=date).update(s2=q)
            elif slot == "s3":
                q = p.s3
                q=q+1
                u = Booking.objects.filter(date=date).update(s3=q)
            elif slot == "s4":
                q = p.s4
                q=q+1
                u = Booking.objects.filter(date=date).update(s4=q)
        except Booking.DoesNotExist:
            print "YES IT IS"
            if slot == "s1":
                u = Booking.objects.create(date=date,s1=1)
                u.save()
            elif slot == "s2":
                u = Booking.objects.create(date=date,s2=1)
                u.save()
            elif slot == "s3":
                u = Booking.objects.create(date=date,s3=1)
                u.save()
            elif slot == "s4":
                u = Booking.objects.create(date=date,s4=1)
                u.save()
        messages.success(request, 'You have booked a slot!')
        return HttpResponseRedirect("/students/home")
    return render(request, "students/index.html", {})

def chart(request):
    if request.method == "POST":
        date = request.POST.get('date')
        dataSource = {}
        dataSource['chart'] = {
            "caption": "Slot Booking",
                "subCaption": "Bar Graph",
                "xAxisName": "Slot",
                "yAxisName": "No.of students",
                "theme": "fusion"
            }
        dataSource['data'] = []
        for key in range(1,5):
          data = {}
          p = Booking.objects.get(date=date)
          s = 's'+str(key)
          data['label'] = s
          if s == "s1":
              data['value'] = p.s1
          elif s == "s2":
              data['value'] = p.s2
          elif s == "s3":
              data['value'] = p.s3
          else:
              data['value'] = p.s4

          dataSource['data'].append(data)

        # Create an object for the Column 2D chart using the FusionCharts class constructor
        column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
        return render(request, 'students/index.html', {'output': column2D.render()})
    return render(request, "students/graph.html", {})
