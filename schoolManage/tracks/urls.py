from django.urls import path
from .views import *
urlpatterns = [
    path('',TrackListView.as_view(),name='trackList' ),
    path('delete/<int:pk>',TrackDeleteView.as_view(),name='trackDelete' ),
    path('add',TrackCreateView.as_view(),name='trackAdd' ),
    path('update/<int:pk>/', TrackUpdateView.as_view(), name='track_update'),

]
