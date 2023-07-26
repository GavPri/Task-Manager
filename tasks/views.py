from django.shortcuts import render, redirect
from .models import Tasks
# Create your views here.


def get_task_list(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        urgency = 'urgency' in request.POST
        Tasks.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            urgency=urgency)

        return redirect('home')
    return render(request, 'add-task.html')


def edit_task(request, task_id):
    return render(request, 'edit-task.html')
