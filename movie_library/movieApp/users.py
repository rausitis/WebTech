from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    
    fname = forms.CharField(max_length=100)
    femail = forms.EmailField()
    fpass = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8)
    frepass = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('fname', 'femail', 'fpass', 'frepass')
    
