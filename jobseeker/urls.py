from django.urls import path
from .import views

urlpatterns = [
    path('jobseekerreg/',views.jobseekerReg,name='jobseekerreg'),
    path('jobseekerlogin/',views.jobseekerlogin,name='jobseekerlogin'),
    path('jobseekerdash/',views.jobseekerdash,name='jobseekerdash'),
    path('jobseekerlogout/',views.jobseekerlogout,name='jobseekerlogout'),
]