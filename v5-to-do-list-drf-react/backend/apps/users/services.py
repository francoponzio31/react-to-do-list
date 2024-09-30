from .models import User


def get_users(offset:int, limit:int, sort:str) -> tuple[list[User], int]:
    if not sort:
        results = User.objects.all()[offset:limit]
    else:
        results = User.objects.all().order_by(sort)[offset:limit]

    total_items = User.objects.count()
    return results, total_items


def get_user_by_id(task_id:int) -> User:
    return User.objects.get(id=task_id)

