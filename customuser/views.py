from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm

def user_register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")
    else:

        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")
def user_profile(request,userid):
    user=CustomUser.objects.get(userid=userid)
    return render(request,'profile.html',{'user':user})