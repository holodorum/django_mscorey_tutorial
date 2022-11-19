from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:#This class gives us a nested namespace for configuration. It will save to model User, and the fields and order are written down in fields. 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Form for User
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    #This class gives us a nested namespace for configuration. It will save to model User, and the fields and order are written down in fields. 
    class Meta:
        model = User
        fields = ['username', 'email']


#Form profile (which only contains the image), but will look like one form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']