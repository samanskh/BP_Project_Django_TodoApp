# tasks/urls.py
from .views import task_list
from django.urls import path
from .views import task_list, home
from .views import home, delete_task, mark_as_done
urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('', home, name='home'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('mark_as_done/<int:task_id>/', mark_as_done, name='mark_as_done'),
]
# tasks/urls.py



