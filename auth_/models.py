from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(verbose_name='Имя', max_length=150)
    surname = models.CharField(verbose_name='Фамилия', max_length=150)
    patronymic = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    email = models.EmailField(verbose_name='Почта')
    is_moderator = models.BooleanField(verbose_name='Модератор', default=0)

    def __str__(self):
        return self.username
