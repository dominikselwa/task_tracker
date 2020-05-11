from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    deadline_date = models.DateField()
    deadline_time = models.TimeField(default=None)
    is_completed = models.BooleanField(default=False)

    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # end_time = models.TimeField(default=None)
    # start_time = models.TimeField(auto_now_add=True)
    # #is_subtask = models.BooleanField(default=False)

    def __str__(self):
        return self.name
