from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bmobr06/', views.bmobr06, name='bmobr06'),
    url(r'^data/', views.data, name='data'),
    url(r'^waves/', views.waves, name='waves'),
    url(r'^currents/', views.currents, name='currents'),
    url(r'^wind/', views.wind, name='wind'),
    url(r'^atmpres/', views.atmpres, name='atmpres'),
	url(r'^airtemp/', views.airtemp, name='airtemp'),
    url(r'^watertemp/', views.watertemp, name='watertemp'),
    url(r'^relumid/', views.relumid, name='relumid'),
    url(r'^contact/', views.contact, name='contact'),
    ]