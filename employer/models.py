from django.db import models

# Create your models here.
class Employerreg(models.Model):
    company_name = models.CharField(max_length=100)
    ower_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    company_type = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.company_name
    
    

class Job(models.Model):

    employer = models.ForeignKey(
        Employerreg,
        on_delete=models.CASCADE
    )

    job_title = models.CharField(max_length=100)

    company_name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    salary = models.CharField(max_length=50)

    experience = models.CharField(max_length=50)

    job_type = models.CharField(max_length=50)

    vacancies = models.IntegerField()

    skills = models.TextField()

    description = models.TextField()

    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title   
    
    
class applied_jobs(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    jobseeker = models.ForeignKey(
        'jobseeker.Jobseekerreg',
        on_delete=models.CASCADE
    )
    resume=models.FileField(upload_to='resumes/',
        null=True,
        blank=True
    )
    cover_letter = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.jobseeker.name     
