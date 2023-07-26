"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import edit_task, toggle_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'), name=''),
    path('edit/<task_id>', edit_task, name='edit'),
    path('toggle/<task_id>', toggle_task, name='toggle'),
    path('delete/<task_id>', delete_task, name='delete')
    # Authentication Path
    path('members/', include('django.contrib.auth.urls'))
    # Members URL
    path('members/', include('members.urls'))
]
