from django.shortcuts import render

from tasks.models import Task


def home(request):
    return render(request, 'website/home.html',
                  {'tasks': Task.objects.filter(parent_task=None)})
