from urllib import request

from django.contrib import messages
from django.shortcuts import render,redirect
from jobseeker.models import Education, Jobseekerreg, Resume, Skill
from mainapp.models import Logininfo


# COMPLETE LOGIN AND REGISTRATION FUNCTIONALITY FOR JOBSEEKER
def jobseekerReg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        
        if Jobseekerreg.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return render(request,'jobseeker/jobseekerregistration.html')
        
        js =Jobseekerreg.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            password=password)
        request.session['jsid']=js.email
        
        return redirect('jobseekerdash')
    return render(request,'jobseeker/jobseekerregistration.html')


def jobseekerlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        js=Jobseekerreg.objects.filter(
            email=email,
            password=password).first()
        if js:
            request.session['jsid']=js.email
            
            Logininfo.objects.create(
                userid=js.email,
                usertype='jobseeker'
            )
            return redirect('jobseekerdash')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request,'jobseeker/jobseekerlogin.html')


def jobseekerdash(request):

    if "jsid" not in request.session:
        return redirect('jobseekerlogin')

    return render(request,'jobseeker/dashboard.html')



def jobseekerlogout(request):
    del request.session['jsid']
    return redirect('home')


# ADD EDUCATIONFUNCTIONALITY FOR JOBSEEKER
def addeducation(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    # Agar education pehle se hai to dobara add na hone do
    if Education.objects.filter(jobseeker=js).exists():
        messages.error(request, "Education details already added. You can only edit them.")
        return redirect("vieweducation")

    if request.method == "POST":

        course = request.POST.get("course")
        college = request.POST.get("college")
        passing_year = request.POST.get("passing_year")
        percentage = request.POST.get("percentage")

        Education.objects.create(
            jobseeker=js,
            course=course,
            college=college,
            passing_year=passing_year,
            percentage=percentage
        )

        messages.success(request, "Education details added successfully.")
        return redirect("myprofile")

    return render(request, "jobseeker/addeducation.html")

def vieweducation(request):
    if "jsid" not in request.session:
        return redirect('jobseekerlogin')
    js=Jobseekerreg.objects.get(
        email=request.session['jsid']
    )
    education=Education.objects.filter(
        jobseeker=js)
    
    context={
        'education':education
    }
    
    
    return render(request,'jobseeker/vieweducation.html',context)   


def editeducation(request, id):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    education = Education.objects.get(id=id)

    if request.method == "POST":

        education.course = request.POST.get("course")
        education.college = request.POST.get("college")
        education.passing_year = request.POST.get("passing_year")
        education.percentage = request.POST.get("percentage")

        education.save()

        return redirect("vieweducation")

    context = {
        "education": education
    }

    return render(
        request,
        "jobseeker/editeducation.html",
        context
    )

def deleteeducation(request,id):

    Education.objects.get(
        id=id
    ).delete()

    return redirect("vieweducation")


def addskill(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    if request.method=="POST":

        skill_name=request.POST.get("skill_name")

        Skill.objects.create(
            jobseeker=js,
            skill_name=skill_name
        )

        return redirect("viewskill")

    return render(request,"jobseeker/addskill.html")


def viewskill(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    skills = Skill.objects.filter(
        jobseeker=js
    )

    context={
        "skills":skills
    }

    return render(
        request,
        "jobseeker/viewskill.html",
        context
    )
    
def editskill(request,id):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    skill = Skill.objects.get(id=id)

    if request.method=="POST":

        skill.skill_name = request.POST.get("skill_name")

        skill.save()

        return redirect("viewskill")

    context={
        "skill":skill
    }

    return render(
        request,
        "jobseeker/editskill.html",
        context
    )
        
    
def deleteskill(request,id):

    Skill.objects.get(
        id=id
    ).delete()

    return redirect("viewskill")   


def uploadresume(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    if request.method=="POST":

        resume=request.FILES.get("resume")

        Resume.objects.create(
            jobseeker=js,
            resume_file=resume
        )

        return redirect("viewresume")

    return render(
        request,
        "jobseeker/uploadresume.html"
    ) 



def viewresume(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    resumes = Resume.objects.filter(
        jobseeker=js
    )

    context = {
        "resumes":resumes
    }

    return render(
        request,
        "jobseeker/viewresume.html",
        context
    )
    

def editresume(request,id):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    resume = Resume.objects.get(id=id)

    if request.method=="POST":

        if request.FILES.get("resume"):

            resume.resume_file = request.FILES.get("resume")

            resume.save()

        return redirect("viewresume")

    context={
        "resume":resume
    }

    return render(
        request,
        "jobseeker/editresume.html",
        context
    )
    
    
def deleteresume(request,id):

    Resume.objects.get(
        id=id
    ).delete()

    return redirect("viewresume")        
 
 
 
def myprofile(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    educations = Education.objects.filter(
        jobseeker=js
    )

    skills = Skill.objects.filter(
        jobseeker=js
    )

    resumes = Resume.objects.filter(
        jobseeker=js
    )

    context = {
        "js": js,
        "educations": educations,
        "skills": skills,
        "resumes": resumes
    }

    return render(
        request,
        "jobseeker/myprofile.html",
        context
    )  
    
    
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Jobseekerreg


def editprofile(request):

    if "jsid" not in request.session:
        return redirect("jobseekerlogin")

    js = Jobseekerreg.objects.get(
        email=request.session["jsid"]
    )

    if request.method == "POST":

        js.name = request.POST.get("name")
        js.email = request.POST.get("email")
        js.mobile = request.POST.get("mobile")

        js.save()

        request.session["jsid"] = js.email

        messages.success(request, "Profile Updated Successfully")

        return redirect("myprofile")

    context = {
        "js": js
    }

    return render(
        request,
        "jobseeker/editprofile.html",
        context
    )      