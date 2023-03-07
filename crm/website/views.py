from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    records = Record.objects.all()
    form = AddRecordForm()
    return render(request,'home.html',{'records':records,'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"Error logging you in!")
        
    return render(request,'auth/login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully...")
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                login(request,user)
                messages.success(request,"Registered successfully")
                return redirect('home')
    else: 
        form = SignUpForm()
        return render(request,'auth/register.html',{'form':form})
    return render(request,'auth/register.html',{'form':form})

@login_required
def customer_record(request,pk):
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None,instance=record)
    return render(request,'customers/show.html',{'record':record,'form':form})

@login_required 
def customer_record_delete(request,pk):
    Record.objects.get(id=pk).delete()
    messages.success(request,"Record was deleted successfully")
    return redirect('home')

@login_required
def add_record(request):
    if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Record added successfully")
                return redirect('home')
    else: 
        messages.error(request,"An error was encountered")
        return redirect('home')
    
@login_required   
def edit_record(request,pk):
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None,instance=record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record successfully updated")
        return redirect("home")
    
 
    
