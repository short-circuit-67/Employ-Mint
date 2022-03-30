from django.contrib.auth.models import User
from userprofiles.models import *
# t = FollowerPairs.objects.all()
# for obj in t:    
#     obj.delete()
#     print('deleted')
for id in range(20):
    for id3 in range(1, id):
        if len(FollowerPairs.objects.filter(followed_id=id3, followed_by=id)):
            print('skipped', id3, id)
            continue
        else:
            user2 = User.objects.filter(id=id)[0]
            user1 = User.objects.filter(id=id3)[0]
            FollowerPairs.objects.create(followed_by=user2, followed_id=user1).save()
            print('Added', id3, id)
