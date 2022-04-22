from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


def registeruser(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            full_name = request.POST.get("full_name")
            password = request.POST.get('password')
            user = User(
                email = email,
                full_name = full_name,
                password = password
            )

            user.set_password(password)
            user.save()
            messages.success(request,'User registered Successfully!!')
            return redirect('login_user')
    except:
        messages.error(request,'Something went wrong!')
        return redirect('register_user')

    return render(request,'accounts/register_user.html')


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)

            if user.is_staff and user.is_active:
                messages.success(request,'User logged in Successfully!!')
                return redirect('/')
        else:
            messages.error(request,'Email/Password is incorrect!!')
            return redirect('login_user')

    return render(request,'accounts/login_user.html')


@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    messages.error(request,'User logged out successfully!!')
    return redirect('login_user')