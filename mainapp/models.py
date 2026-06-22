from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Logininfo(models.Model):
    userid=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    login_time=models.DateTimeField(auto_now_add=True)
    logout_time=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.userid    
