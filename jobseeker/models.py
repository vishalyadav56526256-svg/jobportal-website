from django.db import models

# Create your models here.
class Jobseekerreg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    regdate=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    jobseeker=models.ForeignKey(Jobseekerreg,on_delete=models.CASCADE)
    course=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    passing_year=models.IntegerField()
    percentage=models.FloatField()
    
    def __str__(self):
        return self.course 


class Skill(models.Model):
    jobseeker = models.ForeignKey(
        Jobseekerreg,
        on_delete=models.CASCADE
    )

    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
    
    
    
class Resume(models.Model):
    jobseeker = models.ForeignKey(
        Jobseekerreg,
        on_delete=models.CASCADE
    )

    resume_file = models.FileField(
        upload_to='resumes/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.jobseeker.name   
    
  
  
     

       
    
    
