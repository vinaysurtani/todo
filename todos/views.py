from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import task

# Create your views here.
def addTask(request):
    task1 = request.POST['task']
    task.objects.create(task=task1)
    return redirect('home')