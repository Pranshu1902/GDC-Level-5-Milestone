from re import search
from turtle import title
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task

tasks = []
complete = []

def task_view(request):
    searched = request.GET.get("search")
    task = Task.objects.filter(deleted=False)
    if searched:
        task = task.filter(title__icontains=searched)
    return render(request, "task.html", {"tasks": task})

def add_task_view(request):
    item = request.GET.get("task")
    Task(title=item).save()
    return HttpResponseRedirect('/task')

def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect('/task')

def task_viewer(request):
    task = Task.objects.filter(completed=False)
    return render(request, "show.html", {"tasks": task})

def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    #complete.append(tasks.pop(index-1))
    return HttpResponseRedirect('/task')

def view_complete(request):
    compl = Task.objects.filter(completed=True)
    return render(request, "complete.html", {"complete": compl})

def all_tasks(request):
    all = Task.objects.all()
    return render(request, "all.html", {"all_tasks": all})

def complete_task_id(request, id):
    Task.objects.filter(id=id).update(completed=True)
