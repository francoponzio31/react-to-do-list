from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from utils.utils import get_response_message
from .serializers import TaskOutputSerializer, TaskBodySerializer
from .models import Task
from . import services
import logging


logger = logging.getLogger(__name__)

#! OPCION 1: Un solo wievset dividido en las rutas
class TasksViewSet(ViewSet):

    def get_tasks(self, request):
        try:
            tasks = services.get_tasks()
            tasks_output = TaskOutputSerializer(tasks, many=True)
            return get_response_message(tasks=tasks_output.data, success=True, message="Successful search")
        except Exception as ex:
            logger.exception(ex)
            return get_response_message(status=500, success=False, message="Internal server error")


    def get_task(self, request, task_id):
        try:
            task = services.get_task_by_id(task_id)
            task_output = TaskOutputSerializer(task)
            return get_response_message(task=task_output.data, success=True, message="Successful search")
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_response_message(status=404, success=False, message="Task with the given id not found")
        except Exception as ex:
            logger.exception(ex)
            return get_response_message(status=500, success=False, message="Internal server error")
        

    def create_task(self, request):
        try:
            body_serializer = TaskBodySerializer(data=request.data)
            body_serializer.is_valid(raise_exception=True)
            new_task = services.create_task(**body_serializer.validated_data)
            task_output = TaskOutputSerializer(new_task)
            return get_response_message(task=task_output.data, success=True, message="Successful creation")
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_response_message(errors=body_serializer.errors, status=400, success=False, message="Invalid task data")
        except Exception as ex:
            logger.exception(ex)
            return get_response_message(status=500, success=False, message="Internal server error")


    def update_task(self, request, task_id):
        try:
            body_serializer = TaskBodySerializer(data=request.data, partial=True)
            body_serializer.is_valid(raise_exception=True)
            updated_task = services.update_task(task_id, **body_serializer.validated_data)
            task_output = TaskOutputSerializer(updated_task)
            return get_response_message(task=task_output.data, success=True, message="Successful update")
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_response_message(errors=body_serializer.errors, status=400, success=False, message="Invalid task data")
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_response_message(status=404, success=False, message="Task with the given id not found")
        except Exception as ex:
            logger.exception(ex)
            return get_response_message(status=500, success=False, message="Internal server error")


    def delete_task(self, request, task_id):
        try:
            services.delete_task(task_id)
            return get_response_message(success=True, message="Successful delete")
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_response_message(status=404, success=False, message="Task with the given id not found")
        except Exception as ex:
            logger.exception(ex)
            return get_response_message(status=500, success=False, message="Internal server error")


#! OPCION 2: Dos viewsets distintos para rutas con o sin id
# class TaskListView(APIView):
#     """
#     Vista para listar todos los objetos Task y crear uno nuevo.
#     """

#     def get(self, request):
#         ...

#     def post(self, request):
#         ...

# class TaskDetailView(APIView):
#     """
#     Vista para obtener, actualizar o eliminar un objeto Task específico.
#     """

#     def get(self, request, pk):
#         ...

#     def put(self, request, pk):
#         ...

#     def delete(self, request, pk):
#         ...