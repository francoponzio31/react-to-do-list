from django.urls import path
from . import views


#! OPCION 1: Un solo wievset dividido en las rutas
urlpatterns = [
    path(
        "",
        views.TasksViewSet.as_view({
            "get": "get_tasks",
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


#! OPCION 2: Dos viewsets distintos para rutas con y sin id
# urlpatterns = [
#     path('', TaskListView.as_view(), name='list-create'),  # Listar y crear
#     path('<int:pk>/', TaskDetailView.as_view(), name='detail'),  # Operaciones de detalle: obtener, actualizar, eliminar
# ]