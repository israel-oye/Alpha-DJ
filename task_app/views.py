import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('add-tasks')

    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            user = User.objects.get(username=uname)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("add-task")
        else:
            messages.error(request, "Incorrect username or password")
    ctx = {}
    return render(request, "login.html", context=ctx)


def logout_view(request):
    logout(request)
    return redirect("task-home")


def index(request):
    return render(request, "index-task.html")


def all_tasks(request):
    ctx = {"tasks": Task.objects.all()}
    return render(request, "tasks.html", ctx)


@login_required(login_url="login")
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-home")

    ctx = {"form": form}
    return render(request, "task-form.html", context=ctx)


@login_required(login_url="login")
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.user != task.owner:
        return HttpResponse('You are not allowed here')

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("all-tasks")

    ctx = {"form": form}
    return render(request, "task-form.html", context=ctx)


def delete_task(request, pk):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponse(json.dumps("{'message': 'Login to delete stuff'}"), status=401)
        task = Task.objects.get(id=pk)
        task.delete()
        return HttpResponse(json.dumps("{'message': 'Deleted successfully!'}"), status=200)
    return redirect("all-tasks")
