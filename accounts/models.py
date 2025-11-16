from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    """Пользователь приложения, сотрудник организации"""

    middle_name = models.CharField("Отчество", max_length=150, blank=True)
    uid = models.UUIDField("Уникальный идентификатор 1С", blank=True, null=True, unique=True)
    position = models.CharField("Должность", max_length=255, blank=True)
    department = models.CharField("Подразделение", max_length=255, blank=True)

