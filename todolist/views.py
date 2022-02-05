from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserForm
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.template.loader import get_template
# from project import todolist
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm, UserForm
from django.forms.models import model_to_dict

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
# Create your views here.
def registeration_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Account was created ')

            return redirect('login')
    
    context = {'form': form}
    return render(request, 'todolist/register.html', context)

def todo(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todolist/task.html', context)

def createUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-task')
    context = {'form': form}
    return render(request, 'todolist/register.html', context)

@login_required(login_url='login')
def create(request):
     tasks = Task.objects.filter(user = request.user)
     form = TaskForm()
     if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            print(request.user)
            form.save()
     context = {'form': form, 'tasks': tasks}
     return render(request, 'todolist/task-form.html', context)

def logout_user_page(request):
    logout(request) 
    return redirect('login')

def login_user_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'welcome {username}')
            return redirect('create-task')
        else:
            messages.info(request, 'Wrong username pasword or acc doesnt exist')

    form = AuthenticationForm()
    return render(request, 'todolist/login.html', {'form': form})
    

#update task 
@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(taskId = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('create-task')
    
    context = {'form': form}
    return render(request, 'todolist/task-form.html', context)

#delete task from the list
@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(taskId = pk).delete()
    return redirect('create-task')



def page_not_found_view(request, exception):
    return render(request, 'todolist/404.html', status = 404)