from django.conf.urls import url, include

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^signup', views.SignUp.as_view(), name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]