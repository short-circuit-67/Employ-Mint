from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

for id in range(1, 50): 
    username = 'username' + str(id)
    first_name = 'FirstName_' + username
    last_name = 'LastName_' + username
    password = make_password(password='dummypassword', salt=None, hasher='default')
    about = "About Entry 1 for " + username + "\n"
    edu = "Education  History Entry 1 for " + username + "\n"
    jh = "Job  History Entry 1 for " + username + "\n"
    for entry in range(2, 6):
        about = about + "About Entry " + entry +  " for " + username + "\n"
        edu = edu + "Education  History Entry " + entry +  " for " + username + "\n"
        jh = jh + "Job  History Entry " + entry +  " for " + username + "\n"

    print(username)
    print(password)
    print(first_name)
    print(last_name)
    print(about)
    print(jh)
    print(edu)
    