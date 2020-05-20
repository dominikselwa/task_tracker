from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'name',
                  'description',
                  'start_date',
                  'end_date',
                  'deadline_date',
                  'deadline_time',
                  'is_completed',
                  'parent_task',
                  'owner')
