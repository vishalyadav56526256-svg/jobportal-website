from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employerreg , Job



# Employer Register
def employer_register(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        ower_name = request.POST.get("ower_name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        address = request.POST.get("address")
        company_type = request.POST.get("company_type")
        password = request.POST.get("password")

        # Check duplicate email
        if Employerreg.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("employer_register")

        employer = Employerreg.objects.create(
            company_name=company_name,
            ower_name=ower_name,
            email=email,
            mobile_number=mobile_number,
            address=address,
            company_type=company_type,
            password=password,
        )

        messages.success(request, "Registration Successful. Please Login.")
        return redirect("employer_login")

    return render(request, "employer/register.html")


# Employer Login
def employer_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            employer = Employerreg.objects.get(
                email=email,
                password=password
            )

            request.session["employer_id"] = employer.id

            messages.success(request, "Login Successful")
            return redirect("employer_dashboard")

        except Employerreg.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
            return redirect("employer_login")

    return render(request, "employer/login.html")


# Employer Dashboard
def employer_dashboard(request):

    if "employer_id" not in request.session:
        return redirect("employer_login")

    try:
        employer = Employerreg.objects.get(
            id=request.session["employer_id"]
        )

    except Employerreg.DoesNotExist:
        request.session.flush()
        return redirect("employer_login")

    return render(
        request,
        "employer/dashboard.html",
        {"employer": employer},
    )


# Employer Logout
def logout(request):
    request.session.flush()
    messages.success(request, "Logout Successfully")
    return redirect("employer_login")



def profile(request):
    if "employer_id" not in request.session:
        return redirect("employer_login")
    employer = Employerreg.objects.get(id=request.session["employer_id"])
    return render(request, "employer/profile.html", {"employer": employer})


def edit_profile(request):
    if "employer_id" not in request.session:
        return redirect("employer_login")

    employer = Employerreg.objects.get(id=request.session["employer_id"])

    if request.method == "POST":
        employer.company_name = request.POST.get("company_name")
        employer.ower_name = request.POST.get("ower_name")
        employer.email = request.POST.get("email")
        employer.mobile_number = request.POST.get("mobile_number")
        employer.address = request.POST.get("address")
        employer.company_type = request.POST.get("company_type")
        # employer.password = request.POST.get("password")

        # Check duplicate email
        if Employerreg.objects.filter(email=employer.email).exclude(id=employer.id).exists():
            messages.error(request, "Email already registered.")
            return redirect("edit_profile")

        employer.save()
        request.session["employer_id"] = employer.id  
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    

    return render(request, "employer/edit_profile.html", {"employer": employer})

# JOB POSTING VIEWS
def post_job(request):
    if "employer_id" not in request.session:
        return redirect("employer_login")

    employer = Employerreg.objects.get(id=request.session["employer_id"])

    if request.method == "POST":
        job_title = request.POST.get("job_title")
        company_name = request.POST.get("company_name")
        location = request.POST.get("location")
        salary = request.POST.get("salary")
        experience = request.POST.get("experience")
        job_type = request.POST.get("job_type")
        vacancies = request.POST.get("vacancies")
        skills = request.POST.get("skills")
        description = request.POST.get("description")

        job = Job.objects.create(
            employer=employer,
            job_title=job_title,
            company_name=company_name,
            location=location,
            salary=salary,
            experience=experience,
            job_type=job_type,
            vacancies=vacancies,
            skills=skills,
            description=description,
        )

        messages.success(request, "Job posted successfully.")
        return redirect("employer_dashboard")

    return render(request, "employer/post_job.html", {"employer": employer})



def my_jobs(request):
    if "employer_id" not in request.session:
        return redirect("employer_login")

    employer = Employerreg.objects.get(id=request.session["employer_id"])
    jobs = Job.objects.filter(employer=employer)

    return render(request, "employer/my_jobs.html", {"employer": employer, "jobs": jobs})

def edit_job(request, job_id):
    if "employer_id" not in request.session:
        return redirect("employer_login")

    employer = Employerreg.objects.get(id=request.session["employer_id"])
    job = Job.objects.get(id=job_id, employer=employer)

    if request.method == "POST":
        job.job_title = request.POST.get("job_title")
        # job.company_name = request.POST.get("company_name")
        job.company_name = employer.company_name  # Use the employer's company name
        job.location = request.POST.get("location")
        job.salary = request.POST.get("salary")
        job.experience = request.POST.get("experience")
        job.job_type = request.POST.get("job_type")
        job.vacancies = request.POST.get("vacancies")
        job.skills = request.POST.get("skills")
        job.description = request.POST.get("description")

        job.save()
        messages.success(request, "Job updated successfully.")
        return redirect("my_jobs")

    return render(request, "employer/edit_job.html", {"employer": employer, "job": job})

def delete_job(request, job_id):
    if "employer_id" not in request.session:
        return redirect("employer_login")

    employer = Employerreg.objects.get(id=request.session["employer_id"])
    job = Job.objects.get(id=job_id, employer=employer)

    job.delete()
    messages.success(request, "Job deleted successfully.")
    return redirect("my_jobs")