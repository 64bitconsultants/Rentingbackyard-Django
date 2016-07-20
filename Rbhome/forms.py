__author__ = 'h_hack'
from django import forms
from django.contrib.auth.models import User
from models import Userprofile,BackyardModel

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
            super(Userform, self).__init__(*args, **kwargs)
            for fieldname in ['username', 'email', 'password']:
                self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileform(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('Name','Address', 'Contact')

class Backyardform(forms.ModelForm):
    class Meta:
        model = BackyardModel
        fields = ('state', 'city', 'zip', 'size', 'rent', 'capacity')
