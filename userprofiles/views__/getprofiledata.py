from django.contrib.auth.models import User
from userprofiles.models import About, EducationHistory, FollowerPairs, JobHistory
from jobhandler.models import Applicants, Job

# returns data to be displayed on userprofile pages
def get_profile_data(request, username: str):
    profile_data = {}

    # Get django.contrib.auth.models.User instance
    user_instance_obj: User = User.objects.all().filter(username=username).values()[0]
    user_instance = user_instance_obj['id']
    profile_data['username'] = user_instance_obj['username']
    profile_data['name'] = user_instance_obj['first_name'] + ' ' + user_instance_obj['last_name']
    profile_data['joindate'] = user_instance_obj['date_joined']

    # Get Education History
    eduhistory = EducationHistory.objects.all().filter(user=user_instance).values()[0]['eduhist']
    profile_data['eh'] = eduhistory

    # About
    about = About.objects.all().filter(user=user_instance).values()[0]['about']
    profile_data['ab'] = about
    
    # Get Job History
    jobhistory = JobHistory.objects.all().filter(user=user_instance).values()[0]['jobhist']
    profile_data['jh'] = jobhistory

    # Get Follower Count
    follower_count = FollowerPairs.objects.all().filter(followed_id=user_instance)
    
    profile_data['frc'] = len(follower_count)

    # Get Following Count
    following_count = (FollowerPairs.objects.all().filter(followed_by=user_instance))
    profile_data['fgc'] = len(following_count)

    second_id = request.user.id
    # Is user following this acc
    is_following = len(FollowerPairs.objects.filter(followed_id=user_instance, followed_by=second_id)) > 0
    profile_data['iff'] = is_following

    # Mutuals
    profile_data['mututal_count'] = len(FollowerPairs.objects.filter(followed_id=user_instance).filter(followed_by=second_id))

    #Job Posts
    profile_data['jp'] = get_jobs_posted(user_instance)

    #Job Applications
    profile_data['ja'] = get_job_applications(user_instance)

    profile_data['follow_link'] = username + '/'
    return profile_data

def add_follower(user, follower):
    follower_pair = FollowerPairs(followed_by=follower.id, followed_id=user.id)
    follower_pair.save()

def get_jobs_posted(user):
    return Job.objects.filter(posted_by=user).values('job_id','position', 'company')

def get_job_applications(user):
    applications = Applicants.objects.filter(user=user)
    job_applications = []
    for app in applications:
        job_applications.append({'job_id': app.job.job_id, 'position':app.job.position, 'company': app.job.company})
    return job_applications