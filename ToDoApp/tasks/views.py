# tasks/views.py
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.db.models import Value
from django.db.models.functions import NullIf
from django.shortcuts import render, redirect, get_object_or_404

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
# tasks/views.py


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to refresh the page after adding a task
    else:
        form = TaskForm()

    # Get a list of all days
    days = Task.DAY_CHOICES

    # Get tasks for each day
    tasks_by_day = {day[0]: Task.objects.filter(day=day[0]).order_by('id') for day in days}

    # Zip days and tasks together
    zipped_data = zip(days, tasks_by_day.values())

    return render(request, 'tasks/home.html', {'form': form, 'zipped_data': zipped_data})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('home')

def mark_as_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = True
    task.save()
    return redirect('home')






