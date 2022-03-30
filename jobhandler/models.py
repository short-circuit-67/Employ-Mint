from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

#Stores Job entries
class Job (models.Model):
        job_id = models.AutoField(primary_key=True, unique=True, blank=False )
        position = models.CharField(max_length= 100, blank=False)
        company = models.CharField(max_length= 100, blank=False)
        posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
        requirements = models.CharField(max_length= 1000, blank=False)
        salary_min = models.IntegerField(blank=False)
        salary_max = models.IntegerField(blank=False, null=False)
        post_date =models.DateField(blank=False)

#Stores Job Applications of Users:
class Applicants (models.Model):
        job = models.ForeignKey(Job , on_delete=CASCADE, blank=False )
        user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)


    

