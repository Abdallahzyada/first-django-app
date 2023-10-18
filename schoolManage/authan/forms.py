from django import forms
from .models import *
from django.contrib.auth.forms import *

# class Regform(UserCreationForm):
#     pass


# class Logform(AuthenticationForm):
#     pass

class Regsitrationform(forms.ModelForm):  
    class Meta:
        model=MYUser
        fields='__all__'
        

class Loginform(forms.ModelForm):
    class Meta:
        model=MYUser
        fields=['username','password']
