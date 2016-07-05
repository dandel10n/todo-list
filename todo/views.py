from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def task_list(request):
    tasks = Task.objects.order_by('due_date')
    return render(request, 'todo/index.html', {'tasks': tasks})


def task_info(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_info.html', {'task': task})

@login_required
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            #task.author = request.user
            task.save()
            return redirect('task_info', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'todo/new_task.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            #task.author = request.user
            task.save()
            return redirect('task_info', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/new_task.html', {'form': form})

@login_required
def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo.views.task_list')

@login_required
def task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('todo.views.task_list')
