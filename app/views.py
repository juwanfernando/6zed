from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error!!!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records })

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully register...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def lab(request):
    return render(request, 'lab.html', {})

def query(request):
    return render(request, 'query.html', {})

def batch(request):
    return render(request, 'batch.html', {})

def work_order(request):
    return render(request, 'workOrder.html', {})

def bench_sheet(request):
    return render(request, 'benchSheet.html', {})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "The record deleted successfully...")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
def add_record(request,):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')