from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# create Login Function 
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username!!")
            return redirect('login_page')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password!!")
            return redirect('login_page')

        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login_page.html')


# Create Register Function
def register_page(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        course = request.POST.get('course')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=email)
        if user.exists():
            messages.info((request, 'Email is already taken!!'))
            return redirect('register_page')
        
        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=email, 
                       
        )

        user.set_password(password)
        user.save()

        Profile.objects.filter(user=user).update(course=course)


        messages.success(request, 'Your account created successfully!!')
        return redirect('home')
    
    return render(request, 'register_page.html')


# Create Logout Function
def logout_page(request):
    logout(request)
    return redirect('login_page')