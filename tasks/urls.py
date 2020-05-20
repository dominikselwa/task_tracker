from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.task_details, name='task_detail'),
    path('newtask', views.add_task, name='add_task'),
    path('<int:id>/newsubtask', views.add_subtask, name='add_subtask'),
    path('api/task/', views.TaskListCreate.as_view()),
]
