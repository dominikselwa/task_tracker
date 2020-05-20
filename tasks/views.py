from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Task

from .serializers import TaskSerializer
from rest_framework import generics


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def task_details(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'tasks/task_details.html',
                  {'task': task, 'subtasks': Task.objects.filter(parent_task=Task(pk=id))})


TaskForm = modelform_factory(
    Task, exclude=['end_date', 'is_completed', 'parent_task'])


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html',
                  {'form': form})


def add_subtask(request, id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        subtask = form.save(commit=False)
        subtask.parent_task = Task(pk=id)
        if form.is_valid():
            subtask.save()
            return redirect('task_detail', id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html',
                  {'form': form})
