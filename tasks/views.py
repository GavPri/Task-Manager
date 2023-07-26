from django.shortcuts import render
from .models import Task
# Create your views here.


def get_task_list(request):
    tasks = Task.objects.all()
    context = {
        'task': task
    }
    return render(request, 'tasks.html', context)