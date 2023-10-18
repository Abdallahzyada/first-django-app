from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .forms import *

class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'tracks/track_add.html'
    success_url = "/Track"  


class TrackListView(ListView):
    model=Track
    template_name='tracks/track_list.html'
    context_object_name='tracks'

class TrackDeleteView(DeleteView):
    model=Track
    template_name='tracks/confirm_delete.html'
    success_url ="/Track"


class TrackUpdateView(UpdateView):
    model = Track
    form_class = TrackForm
    template_name = 'tracks/track_add.html'
    success_url = "/Track" 

