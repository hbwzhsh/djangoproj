from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bmobr06/', views.bmobr06, name='bmobr06'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^data/', views.data, name='data'),
    url(r'^waves/', views.waves, name='waves'),
]