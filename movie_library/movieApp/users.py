from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenum = forms.NumberInput()
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Re-enter Password:', widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('fname', 'lname', 'email', 'password1', 'password2')
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs.update({'class': 'entryField'})
        self.fields['lname'].widget.attrs.update({'class': 'entryField'})
        self.fields['email'].widget.attrs.update({'class': 'entryField'})
        self.fields['password1'].widget.attrs.update({'class': 'entryField'})
        self.fields['password2'].widget.attrs.update({'class': 'entryField'})
