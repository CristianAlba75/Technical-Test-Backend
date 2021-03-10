from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),                                # Welcome url
    path('get_tasks', views.get_tasks, name='get_tasks'),                            # Get user tasks url
    path('add_task', views.add_task, name='add_task'),                              # Add task url
    path('update_task/<int:task_id>', views.update_task, name='update_task'),          # Update task url
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),          # Delete task url
    path('search_task', views.search_by_description, name='search_task'),              # Search task url
    path('change_state/<int:task_id>', views.change_status_task, name='change_state'),  # Search task url
]
