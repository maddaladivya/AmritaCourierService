from django.conf.urls import url, include

from . import views
from django.views.generic.base import TemplateView
from manager import views
from manager.views import home
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^home', home.as_view(), name='managerhome'),
    url(r'^mail', views.Order, name='mail'),
    url(r'^addrollno', views.addRollNo, name='addrollno'),
    url(r'^deliver', views.deliverCourier, name='deliver'),
    url(r'^managerlogin$', views.managerLogin, name='managerlogin'),
    url(r'^managerlogout$', views.managerLogout, name='managerlogout')
]
