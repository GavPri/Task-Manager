from django.shortcuts import render
from .models import Tasks
# Create your views here.


def get_task_list(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)


def add_task(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'add-task.html')
