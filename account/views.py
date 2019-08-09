from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from account.models import Profile
# Create your views here.

def corporation(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password'])
            auth.login(request, user)

            profile = Profile()
            profile.user = user
            profile.master = True
            profile.save()

            return redirect('home')
    return render(request, 'accounts/corporation.html')

def individual(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            
            profile = Profile()
            profile.user = user
            profile.master = False
            profile.save()

            return redirect('home')
    return render(request, 'accounts/individual.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')