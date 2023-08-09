from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordFrom
from .models import Record


def home(request):
    # this is the records model
    records = Record.objects.all()
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
        return render(request,'home.html',{'records':records})

# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')
def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully Logged in ")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be  Logged in ")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_id = Record.objects.get(id=pk)
        delete_id.delete()
        messages.success(request,"Record Delete Sucessfully")
        return redirect('home')
    else:
         messages.success(request,"you must br logged in")
         return redirect('home')
def add_record(request):
    form = AddRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New record saved")
                return redirect('home')
        return render(request, 'addrecord.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('home')
def update_record(request,pk):
      if request.user.is_authenticated:
          current_record = Record.objects.get(id=pk)
          form = AddRecordFrom(request.POST or None,instance=current_record)   # using a instance to pass the data into  the page
          if form.is_valid():
              form.save()
              messages.success(request, "Record Updated Successfully ")
              return redirect('home')
          return render(request, 'update_record.html', {'form': form})
      else:
        messages.success(request, "You must be logged in...")
        return redirect('home')
          




