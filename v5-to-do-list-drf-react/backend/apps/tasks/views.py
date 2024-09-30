from rest_framework.viewsets import ViewSet
from rest_framework.serializers import ValidationError
from rest_framework import status
from utils.custom_responses import get_success_response, get_error_response
from .serializers import TaskOutputSerializer, TaskBodySerializer
from utils.common_serializers import PaginationParamsSerializer
from .models import Task
from . import services
import logging


logger = logging.getLogger(__name__)

class TasksViewSet(ViewSet):

    def get_current_user_tasks(self, request):
        try:
            current_user_id = request.user.id
            params_serializer = PaginationParamsSerializer(
                data=request.query_params,
                context={"valid_fields": ["id", "done", "text", "created_at", "user_id"]}
            )
            params_serializer.is_valid(raise_exception=True)
            tasks, total_items = services.get_user_tasks(current_user_id, **params_serializer.validated_data)
            tasks_output = TaskOutputSerializer(tasks, many=True)
            return get_success_response(status=status.HTTP_200_OK, tasks=tasks_output.data, total=total_items)
        except ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid search data", errors=params_serializer.errors)
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_task(self, request, task_id):
        try:
            task = services.get_task_by_id(task_id)
            task_output = TaskOutputSerializer(task)
            return get_success_response(status=status.HTTP_200_OK, task=task_output.data)
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_404_NOT_FOUND, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def create_task(self, request):
        try:
            body_serializer = TaskBodySerializer(data=request.data)
            body_serializer.is_valid(raise_exception=True)
            new_task = services.create_task(user_id=request.user.id, **body_serializer.validated_data)
            task_output = TaskOutputSerializer(new_task)
            return get_success_response(status=status.HTTP_201_CREATED, task=task_output.data)
        except ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid task data", errors=body_serializer.errors)
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update_task(self, request, task_id):
        try:
            body_serializer = TaskBodySerializer(data=request.data, partial=True)
            body_serializer.is_valid(raise_exception=True)
            updated_task = services.update_task(task_id, **body_serializer.validated_data)
            task_output = TaskOutputSerializer(updated_task)
            return get_success_response(status=status.HTTP_200_OK, task=task_output.data)
        except ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid task data", errors=body_serializer.errors)
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_404_NOT_FOUND, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete_task(self, request, task_id):
        try:
            services.delete_task(task_id)
            return get_success_response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_404_NOT_FOUND, message=f"Task with id {task_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
