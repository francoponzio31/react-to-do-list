from .models import Task
from apps.users.models import User


def get_user_tasks(user_id:int, offset:int, limit:int, sort:str) -> tuple[list[Task], int]:

    queryset = Task.objects.filter(user=user_id)

    if sort:
        queryset = queryset.order_by(sort)

    total_items = Task.objects.count()

    tasks = queryset[offset:offset+limit]

    return tasks, total_items


def get_task_by_id(task_id:int) -> Task:
    return Task.objects.get(id=task_id)


def create_task(text:str, user_id=int) -> Task:
    user = User.objects.get(id=user_id)
    return Task.objects.create(text=text, user=user)


def update_task(task_id:int, **kwargs) -> Task:
    task = Task.objects.get(id=task_id)
    for key, value in kwargs.items():
        setattr(task, key, value)
    task.save()
    return task


def delete_task(task_id:int) -> None:
    task = Task.objects.get(id=task_id)
    task.delete()
