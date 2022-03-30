from django import forms

# django Form used for posting jobs
class Job_Post_form (forms.Form):
    position  = forms.CharField(max_length=100)
    company = forms.CharField(max_length= 100)
    requirements = forms.CharField(max_length=500,widget=forms.Textarea())
    salary_min = forms.IntegerField()
    salary_max = forms.IntegerField()    
