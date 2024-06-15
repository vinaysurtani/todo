from django.shortcuts import render
from todos.models import task

def home(request):
    tasksp = task.objects.filter(is_completed = False).order_by('-updated_at')
    tasksc = task.objects.filter(is_completed = True).order_by('-updated_at')
    context = {
        'tasksp' : tasksp,
        'tasksc' : tasksc,
    }
    return render(request,'home.html',context=context)