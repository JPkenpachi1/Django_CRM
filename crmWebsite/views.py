from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    # check the login
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate function
        user = authenticate(request,username=username,password=password) # this is used to check the backend for if the user is registered 
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in")
            return redirect('home')
        else:
            messages.success(request,"your not logged in .....")
            return redirect('home')
    else:
        return render(request,'home.html',{})

# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')
def register_user(request):
    return render(request,'register.html',{})

