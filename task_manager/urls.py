from django.contrib import admin
from django.urls import path

from tasks.views import delete_task_view, task_view, add_task_view, delete_task_view, task_viewer, complete_task_view, view_complete, all_tasks, complete_task_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path("task", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("tasks/", task_viewer),
    path("complete_task/<int:index>/", complete_task_view),
    path("complete_task/<str:id>/", complete_task_id),
    path("completed_tasks", view_complete),
    path("all_tasks", all_tasks),
    path("completed_tasks/", view_complete)
]
