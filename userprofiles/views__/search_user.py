from django.contrib.auth.models import User
from userprofiles.models import FollowerPairs, About, EducationHistory, JobHistory

# returns data for matches in user search
def search_user_results (search_string) :
    search_result = {"name" : [], "abtetc" : []} # Final search results
    sr1 = User.objects.all().filter(username__contains = search_string) # Search results for username matches

    # Search results for each word in the string
    strlst = search_string.split()
    for s in strlst:
        sr1 = sr1.union( User.objects.all().filter(first_name__contains = s))
        sr1 = sr1.union( User.objects.all().filter(last_name__contains = s))
    for obj in sr1 :
        follower_count = FollowerPairs.objects.all().filter(followed_id=obj.id)
        following_count = FollowerPairs.objects.all().filter(followed_by=obj.id)
        context = {
        'id' : obj.id,
        'username' : obj.username,
        'name' : obj.first_name + " " + obj.last_name,
        'joindate' : obj.date_joined,
        'followers' : len(follower_count),
        'following' : len(following_count)
        }
        search_result['name'].append(context)

    # Search resutls for matching about, education history, job historyy
    sr2 = About.objects.all().filter(about__contains = search_string).union(EducationHistory.objects.all().filter(eduhist__contains = search_string), JobHistory.objects.all().filter(jobhist__contains =search_string), all=False)
    lst =[]
    for obj in sr2 :
        lst.append(obj.id)
    ids = (list(set(lst)))
    for x in ids:
        usr = User.objects.all().filter(id = x)
        for obj in usr:
            follower_count = FollowerPairs.objects.all().filter(followed_id=obj.id)
            following_count = FollowerPairs.objects.all().filter(followed_by=obj.id)
            context = {
                'id' : obj.id,
                'username' : obj.username,
                'name' : obj.first_name + " " + obj.last_name,
                'joindate' : obj.date_joined,
                'followers' : len(follower_count),
                'following' : len(following_count)
            }
            search_result['abtetc'].append(context)
    return search_result