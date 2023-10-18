from django.urls import path

from instr.views import *

urlpatterns = [
    path('/List', List, name='instractorList'),
    path('/Add', Add, name='instrcAdd'),
    path('/Update/<int:id>', Update, name='instrcUpdatee'),
    path('/Delete/<int:id>', Delete, name='instrcDelete'),
    path('/List/<int:id>',Listbyid,name='Listbyid'),

]