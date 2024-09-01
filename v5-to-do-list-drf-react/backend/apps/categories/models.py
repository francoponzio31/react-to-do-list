from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.name