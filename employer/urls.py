from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.employer_register, name='employer_register'),
    path('login/', views.employer_login, name='employer_login'),
    path('logout/', views.logout, name='employer_logout'),
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post_job/', views.post_job, name='post_job'),
    path('my_jobs/', views.my_jobs, name='my_jobs'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('view_applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('accept_application/<int:app_id>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:app_id>/', views.reject_application, name='reject_application'),
]