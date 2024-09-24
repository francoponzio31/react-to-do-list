from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.TasksViewSet.as_view({
            "get": "get_current_user_tasks",
            "post": "create_task",
        })
    ),
    path(
        "<int:task_id>/",
        views.TasksViewSet.as_view({
            "get": "get_task",
            "patch": "update_task",
            "delete": "delete_task",
        })
    ),
]
