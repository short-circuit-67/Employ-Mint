from userprofiles.forms import UserSignUp
from django.shortcuts import render

def signup_GET(request):
    form_signup = UserSignUp()
    context = {'form': form_signup}
    return render(request, 'dform_signup.html', context)