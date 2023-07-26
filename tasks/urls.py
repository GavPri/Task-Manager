from django.urls import path

urlpatterns = [
    path('tasks', views.get_task_list, name='tasks')
]
