from django import forms
from tracks.models import *
class addtraineeform(forms.Form):
    name=forms.CharField(max_length=50,label='Name',help_text='enter trainee name name '
                           ,  widget
                             =
                                 forms.TextInput(attrs={'placeholder':'enter trainee name','style':'border-raduis:15%'})
                             )
    tracks=forms.ChoiceField(choices=
                                [(track.id,track.name)
                                 for track in  Track.objects.all()
                                 ])