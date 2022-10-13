from turtle import title
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import TaskForm
from datetime import date, datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Views
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    return render(request, "todolist.html")

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))

@csrf_exempt
def add_task_async(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        #Get the posted form
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = date.today()
            task.save()
    return JsonResponse({"success": "Task is successfully added"}) 

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        #Get the posted form
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = date.today()
            task.save()
        return redirect("todolist:show_todolist")
    context = {'form':form}
    return render(request, "create-task.html", context)



# Form registrasi
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Form login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist')) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Form logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response