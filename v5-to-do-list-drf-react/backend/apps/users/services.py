from .models import User


def get_users(offset:int, limit:int, sort:str) -> tuple[list[User], int]:

    queryset = User.objects.all()

    if sort:
        queryset = queryset.order_by(sort)

    total_items = User.objects.count()

    users = queryset[offset:offset+limit]

    return users, total_items


def get_user_by_id(task_id:int) -> User:
    return User.objects.get(id=task_id)

