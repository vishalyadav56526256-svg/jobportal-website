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
    
    
    
