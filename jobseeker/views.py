from pyexpat.errors import messages

from django.shortcuts import render,redirect

from jobseeker.models import Jobseekerreg
from mainapp.models import Logininfo

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
    return render(request,'jobseeker/jobseekerlogin.html')


def jobseekerdash(request):

    if "jsid" not in request.session:
        return redirect('jobseekerlogin')

    return render(request,'jobseeker/dashboard.html')



def jobseekerlogout(request):
    del request.session['jsid']
    return redirect('home')
