from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from jobhandler.view__.search_job import search_job_results
from .forms import Job_Post_form
from .models import Applicants, Job
from django.contrib.auth.models import User
from datetime import date

# return page to post jobs (/postjob/)
def job_post(request: HttpRequest):
    post_form: Job_Post_form = Job_Post_form()
    context: dict[str: Job_Post_form] = {"form" : post_form }
    if request.method == "POST":
        post_form = Job_Post_form(request.POST)
        if request.user.is_anonymous:
                return redirect('../login/')
        if post_form.is_valid():
            post_dict= post_form.cleaned_data
            post_dict["post_date"] = date.today()
            post_dict["posted_by"] = request.user
            Job.objects.create(**post_dict).save()
            return redirect('../jobs/')
    return render( request , 'Post_Job.html', context)


#returns page for all jobs (/jobs/)
def jobprofile_page(request: HttpRequest):
    passed_list: dict[str: list] = { "list" : []}
    for obj in Job.objects.all():
        context = {
            'id' : obj.job_id,
            'Position' : obj.position,
            'Company' : obj.company,
            'Posted_by' :  obj.posted_by.get_username(),
            'salary_min' : obj.salary_min,
            'salary_max' : obj.salary_max,
            'req': obj.requirements,
            'application_link': '/apply/' + str(obj.job_id) + '/'
        }
        passed_list["list"].append(context)
    return render(request, 'JobProfile.html', passed_list )


# Add application entry to userprofiles_applicants table and redirect to 
def apply_for(request: HttpRequest, job_id: int):
    user_instance_obj: User = request.user
    if user_instance_obj.is_anonymous:
        print('not logged in')
        return redirect('/login')
    job = Job.objects.filter(job_id=job_id)[0]
    Applicants.objects.create(job=job, user=request.user).save()
    return redirect('/jobs')
