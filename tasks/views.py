from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForm
# Create your views here.


def get_task_list(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'add-task.html')


def edit_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'edit-task.html', context)
