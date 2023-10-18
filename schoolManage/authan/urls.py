from django.contrib import admin
from django.urls import path

from authan.views import *

urlpatterns = [
    path('/Login', Login, name='login'),
    path('/Register', Register, name='register'),
    path('/Logout', Logout, name='logout'),

]