from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_task_list, name='home')
]
