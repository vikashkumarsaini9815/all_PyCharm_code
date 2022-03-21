#from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
   # url(r'^home/$', home, name='file-upload'),
   # url(r'^upload/$', FileView.as_view(), name='file-upload'),
    path('home/', home, name='file-upload'),
    path('upload/', FileView.as_view(), name='file-upload'),
]