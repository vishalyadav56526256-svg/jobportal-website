from django.urls import path
from .import views


urlpatterns = [
    path('jobseekerreg/',views.jobseekerReg,name='jobseekerreg'),
    path('jobseekerlogin/',views.jobseekerlogin,name='jobseekerlogin'),
    path('jobseekerdash/',views.jobseekerdash,name='jobseekerdash'),
    path('jobseekerlogout/',views.jobseekerlogout,name='jobseekerlogout'),
    
    

    path("education/add/",views.addeducation,name="addeducation"),
    path("education/view/",views.vieweducation,name="vieweducation"),
    path("education/edit/<int:id>/",views.editeducation,name="editeducation"),
    path("education/delete/<int:id>/",views.deleteeducation,name="deleteeducation"),
    path("myprofile/",views.myprofile,name="myprofile"),
    path("myprofile/edit/",views.editprofile,name="editprofile"),

    path("skill/add/",views.addskill,name="addskill"),
    path("skill/view/",views.viewskill,name="viewskill"),
    path("skill/edit/<int:id>/",views.editskill,name="editskill"),
    path("skill/delete/<int:id>/",views.deleteskill,name="deleteskill"),

    path("resume/upload/",views.uploadresume,name="uploadresume"),
    path("resume/view/",views.viewresume,name="viewresume"),
    path("resume/edit/<int:id>/",views.editresume,name="editresume"),
    path("resume/delete/<int:id>/",views.deleteresume,name="deleteresume"),
]