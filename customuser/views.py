from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import UserSerializer


@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'user_id': "su"}).data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")
    else:

        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


def user_profile(request, userid):
    user = CustomUser.objects.get(userid=userid)
    return render(request, 'profile.html', {'user': user})
