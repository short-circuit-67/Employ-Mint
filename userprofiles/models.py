from django.db import models
from django.contrib.auth.models import User

# Edge List follower graph (edgelist from followed_by -> followed_id)
class FollowerPairs(models.Model):
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')
    followed_id = models.ForeignKey(User , on_delete=models.CASCADE, related_name='followed_id')

# 'About' details for users
class About (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500, blank=True)

# Education history for users
class EducationHistory (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eduhist = models.CharField(max_length=500)

# Job history for users
class JobHistory (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobhist = models.CharField(max_length=500)
