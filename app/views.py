from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, NewProjectForm, AddSampleForm, StoreForm
from .models import Record, Project, Sample, Store
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.template import RequestContext


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
        return render(request, 'home.html', {})
        #return render(request, 'home.html', {'records': records })

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
    
def new_project(request):
    form = NewProjectForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Project has been added...")
                return redirect('all_projects')
        return render(request, 'new_project.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
def all_projects(request):
    projects = Project.objects.all()
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
        return render(request, 'all_projects.html', {'projects':projects})
    
def project(request, pk):
    if request.user.is_authenticated:
        project = Project.objects.get(id=pk)
        return render(request, 'project.html', {'project':project})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('all_projects')
    
def update_project(request, pk):
    if request.user.is_authenticated:
        current_project = Project.objects.get(id=pk)
        form = NewProjectForm(request.POST or None, instance=current_project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project has been updated...")
            return redirect('all_projects')
        return render(request, 'update_project.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
def delete_project(request, pk):
    if request.user.is_authenticated:
        delete_it = Project.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "The record deleted successfully...")
        return redirect('all_projects')
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')

def new_sample(request, add=1):
    form = AddSampleForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Sample has been added...")
                if add == 1:
                    samples = Sample.objects.filter(project_number=form.cleaned_data['project_number'])
                    return render(request, 'new_samples.html', {'samples':samples})
                elif add == 0:
                    return redirect('new_sample')
        return render(request, 'new_sample.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')
    
    
def new_samples(request):
    #samples = Sample.objects.filter(project_number=pn)
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
        return render(request, 'new_samples.html', {})
    
def sample(request, pn=None):
    samples = Sample.objects.filter(project_number=pn)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('new_samples')
        else:
            messages.success(request, "There was an error!!!")
            return redirect('home')
    else:
        return render(request, 'new_samples.html', {'samples':samples})
    
def samples(request, pnum=None):
    projects = Project.objects.all()
    samples = Sample.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('new_samples')
        else:
            messages.success(request, "There was an error!!!")
            return redirect('home')
    else:
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            pnum = request.GET.get('pn')
            context = []
            pid = Project.objects.filter(project_number=pnum).values()[0]['id']
            for sample in Sample.objects.filter(project_number_id=pid).values():
                context.append([pnum, sample['sample_number'], sample['sample_name'], sample['id']])
            return JsonResponse({'data': context})
            #ValueError:
            return JsonResponse(data)
        return render(request, 'samples.html', {'projects':projects,'samples':samples})

def approvals(request):
    projects = Project.objects.all()
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
        return render(request, 'approvals.html', {'projects':projects})
    
def store(request):
    form = StoreForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Store has been added...")
                return redirect('home')
        return render(request, 'store.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page!!!")
        return redirect('home')



from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import Person, City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'list.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'list.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)