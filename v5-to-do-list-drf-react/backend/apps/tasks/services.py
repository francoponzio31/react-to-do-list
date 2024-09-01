from .models import Task


def get_tasks() -> list[Task]:
    return Task.objects.all()

def get_task_by_id(task_id:int) -> Task:
    return Task.objects.get(id=task_id)

def create_task(text:str) -> Task:
    return Task.objects.create(text=text)

def update_task(task_id:int, **kwargs) -> Task:
    task = Task.objects.get(id=task_id)
    for key, value in kwargs.items():
        setattr(task, key, value)
    task.save()
    return task

def delete_task(task_id:int) -> None:
    task = Task.objects.get(id=task_id)
    task.delete()
