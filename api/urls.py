from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTasks, name='get_all_tasks'),
    path('tasks/add/', views.addTasks, name='add_task'),
    path('tasks/<int:pk>/', views.getTask, name='get_task_by_id'),
    path('tasks/<int:pk>/delete/', views.deleteTask, name='delete_task_by_id'),
    path('tasks/<int:pk>/update/', views.updateTask, name='update_task_by_id')
]