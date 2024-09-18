from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from utils.utils import get_success_response, get_error_response
from .serializers import TaskOutputSerializer, TaskBodySerializer
from .models import Task
from . import services
import logging


logger = logging.getLogger(__name__)

class TasksViewSet(ViewSet):

    def get_tasks(self, request):
        try:
            tasks = services.get_tasks()
            tasks_output = TaskOutputSerializer(tasks, many=True)
            return get_success_response(status=200, message="Successful search", tasks=tasks_output.data)
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=500, message="Internal server error")


    def get_task(self, request, task_id):
        try:
            task = services.get_task_by_id(task_id)
            task_output = TaskOutputSerializer(task)
            return get_success_response(status=200, message="Successful search", task=task_output.data)
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=404, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=500, message="Internal server error")
        

    def create_task(self, request):
        try:
            body_serializer = TaskBodySerializer(data=request.data)
            body_serializer.is_valid(raise_exception=True)
            new_task = services.create_task(**body_serializer.validated_data)
            task_output = TaskOutputSerializer(new_task)
            return get_success_response(status=201, message="Successful creation", task=task_output.data)
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=400, message="Invalid task data", errors=body_serializer.errors)
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=500, message="Internal server error")


    def update_task(self, request, task_id):
        try:
            body_serializer = TaskBodySerializer(data=request.data, partial=True)
            body_serializer.is_valid(raise_exception=True)
            updated_task = services.update_task(task_id, **body_serializer.validated_data)
            task_output = TaskOutputSerializer(updated_task)
            return get_success_response(status=200, message="Successful update", task=task_output.data)
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=400, message="Invalid task data", errors=body_serializer.errors)
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=404, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=500, message="Internal server error")


    def delete_task(self, request, task_id):
        try:
            services.delete_task(task_id)
            return get_success_response(status=204, message=f"Task with id {task_id} deleted")
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=404, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=500, message="Internal server error")
