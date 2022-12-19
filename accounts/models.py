from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # fields will be added later
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )

    def __str__(self):
        return f"{self.pk}:) {self.username}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
