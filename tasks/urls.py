from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_task_list, name='home'),
    path('add-task', views.add_task, name='add'),
    path('edit-task', views.edit_task, name='add')
]
