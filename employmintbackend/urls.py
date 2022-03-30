from django.urls import path
from jobhandler.views import jobprofile_page, apply_for, job_post
from userprofiles.views import home_page, login_page, logout_user, nav_bar_search_redirect, profile_page,myfriends, sign_up, follow_user, delete_job, unapply_job, search 

urlpatterns = [
    path('', home_page), 
    path('jobs/', jobprofile_page),
    path('login/', login_page),
    path('logout/', logout_user),
    path('signup/', sign_up),
    path('search/', nav_bar_search_redirect),
    path('postjob/', job_post),
    path('profiles/', follow_user),
    path('apply/<int:job_id>/', apply_for),
    path('profiles/<str:username>', profile_page),
    path('search/<str:search_string>', search),
    path('profiles/delete_job/<int:job_id>/', delete_job),
    path('profiles/unapply_job/<int:job_id>/', unapply_job),
    path('profiles/<str:username>/followers/', myfriends),
]
