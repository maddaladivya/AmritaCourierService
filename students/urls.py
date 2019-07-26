from django.conf.urls import url, include

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^signup', views.SignUp.as_view(), name='signup'),
    url(r'^profile/(?P<pk>[0-9]+)', views.Profile_view, name='profile'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^home', TemplateView.as_view(template_name='students/home.html'), name='home'),
    url(r'^details', views.StudentDetails.as_view(), name='details'),
    url(r'^ticket', views.TicketGenerate.as_view(), name="ticket"),
    url(r'^update', views.UpdateDetails.as_view(), name="update"),
    url(r'^publicpage', views.PublicPage.as_view(), name="public"),
    url(r'^book$', views.book, name='book'),
    url(r'^graph$', views.chart, name='graph'),
    url(r'^ticketsuccessful', TemplateView.as_view(template_name='students/ticketsuccessful.html'), name="suctik")
]
