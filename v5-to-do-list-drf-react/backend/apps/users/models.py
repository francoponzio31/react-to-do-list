from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=256)
    password = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username