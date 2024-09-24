from .models import User


def get_users() -> list[User]:
    return User.objects.all()

def get_user_by_id(task_id:int) -> User:
    return User.objects.get(id=task_id)

