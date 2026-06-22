from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enquiry

# Home Page
def home(request):
    return render(request, "mainapp/home.html")


# About Page
def about(request):
    return render(request, "mainapp/about.html")


# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        Enquiry.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            message=message
        )

        messages.success(request, "Your enquiry has been submitted successfully.")
        return redirect("contact")

    return render(request, "mainapp/contact.html")


# Login Selection Page
def login(request):
    return render(request, "mainapp/login.html")


# Registration Selection Page
def registration(request):
    return render(request, "mainapp/registration.html")

# Create your views here.
