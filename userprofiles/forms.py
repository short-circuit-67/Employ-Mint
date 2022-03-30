from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignUp (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1970, 2022)))
    eduhist = forms.CharField(widget=forms.Textarea())
    jobhist = forms.CharField(widget=forms.Textarea())
    about = forms.CharField(widget=forms.Textarea())
