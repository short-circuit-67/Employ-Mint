from django.contrib.auth.models import User
from userprofiles.models import JobHistory, EducationHistory, About

# save user datat to database from form_signup form
def save_user_data(request, form_signup):
    form_signup.save()
    user_created = User.objects.filter(username=form_signup.cleaned_data['username'])[0]
    EducationHistory.objects.create(id=None, user=user_created, eduhist=request.POST['eduhist']).save()
    JobHistory.objects.create(user=user_created, jobhist=request.POST['jobhist']).save()
    About.objects.create(user=user_created, about=request.POST['about']).save()

    return user_created