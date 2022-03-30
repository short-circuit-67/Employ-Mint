from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from jobhandler.models import Applicants, Job
from jobhandler.view__.search_job import search_job_results
from userprofiles.forms import UserSignUp
from userprofiles.models import FollowerPairs
from userprofiles.views__.save_user_data import save_user_data
from .views__.getprofiledata import get_profile_data
from .views__.signup_GET import signup_GET
from .views__.search_user import search_user_results

# returns profile page fro every user account
def profile_page(request, username: str):
    pd = get_profile_data(request, username)
    return render(request, 'profilepage.html', pd)

# Manage signup page GET and POST requests
def sign_up(request):
    if request.method == 'GET':
        return signup_GET(request)
    else:
        form_signup = UserSignUp(request.POST)
        if not form_signup.is_valid():
            return render(request, 'dform_signup.html', {'form':form_signup})
        user_instance: User = save_user_data(request, form_signup)
        login(request, user_instance)
        return redirect('../profiles/%s'%user_instance.get_username())

# Add/Remove follow entry if logged in and redirect to prev page, else redirect to login page
def follow_user(request):
    if request.method == 'POST':
        user = request.user
        followed_id_username = request.POST.get('followed_id')
        if user.is_anonymous:
            print('not logged in')
            return HttpResponseRedirect('../login')
        else:
            followed_user_instance = User.objects.filter(username=followed_id_username)[0]
            follow_pairs = FollowerPairs.objects.filter(followed_by=user, followed_id=followed_user_instance)
            if len(follow_pairs) == 0:
                FollowerPairs.objects.create(followed_by=user, followed_id=followed_user_instance).save()
                print('Added follower')
            else:
                follow_pairs.delete()
                print('removed follower')
            return redirect('/profiles/'+ followed_user_instance.get_username())
    else:
        return Http404

# return the login page and authenticate login requests
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('auth_username')
        password = request.POST.get('auth_password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print('User logged in: ', user.get_username())
            return HttpResponseRedirect('../profiles/' + user.get_username())
        else:
            print('Login failed')
            return render(request, 'login.html', {'message': 'Incorrect login credentials'})
    return render(request, 'login.html', {})

# return homepage
def home_page(request):
    return render(request, 'home.html', {})

# Remove job post from current user
def delete_job(request, job_id):
    job = Job.objects.filter(job_id=job_id)
    for curr in job:
        curr.delete()
    return redirect('../../' + request.user.get_username())

# Remove job application from current user
def unapply_job(request, job_id):
    job = Applicants.objects.filter(user=request.user.id, job=job_id)
    for curr in job:
        curr.delete()
    return redirect('../../' + request.user.get_username())

# render and return search results
def search(request, search_string):
    job_results = search_job_results(search_string)
    user_results = search_user_results(search_string)
    results = {"jr" : job_results, "ur" : user_results} 
    return render(request, "search_all.html", results)

# Show search results from navbar search bar
def nav_bar_search_redirect(request):
    search_string = request.GET['search_string']
    if search_string:
        return redirect('../search/' + search_string)

# log user out
def logout_user(request):
    logout(request)
    return redirect('/')

def myfriends(request, username : str ):
    user_instance_obj: User = User.objects.filter(username=username).values()[0]
    user_instance = user_instance_obj['id']
    following_count = (FollowerPairs.objects.filter(followed_by=user_instance).values('followed_id_id'))
    followers_count = (FollowerPairs.objects.filter(followed_id=user_instance).values('followed_by_id'))
    friendlist = {"frnd" : []}
    sr2 = followers_count.intersection(following_count)
    sr1=[]
    for x in sr2:
        sr1.append(x['followed_by_id'])

    for obj in sr1 :
        follower_count = FollowerPairs.objects.all().filter(followed_id=obj)
        following_count = FollowerPairs.objects.all().filter(followed_by=obj)
        usr = User.objects.filter(id=obj)[0]
        context = {
        'id' : obj,
        'username' : usr.get_username(),
        'name' : usr.first_name + " " + usr.last_name,
        'joindate' : usr.date_joined,
        'followers' : len(follower_count),
        'following' : len(following_count)
        }
        friendlist['frnd'].append(context)

    return render(request, "followers.html", friendlist)
