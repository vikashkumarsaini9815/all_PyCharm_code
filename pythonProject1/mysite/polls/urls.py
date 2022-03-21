from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('add',views.add,name='add'),
    path('', views.home, name='index'),
    path('admin/', admin.site.urls),
]