from django.db import models
from auth_.models import User


class Post(models.Model):   # Доктор
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='post/%Y/%m/%d/', verbose_name='Изображение')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    experience = models.IntegerField(verbose_name='Стаж')
    category = models.CharField(max_length=150, verbose_name='Категория')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return self.name


class Proposal(models.Model):
    class Status(models.TextChoices):
        Waiting = 'Ожидание', 'Ожидание'
        Accepted = 'Принято', 'Принято'
        Rejected = 'Отклонено', 'Отклонено'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    type = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='proposals', verbose_name='Доктор')
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.Waiting, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    visit_time = models.DateTimeField(verbose_name='Время посещения')


    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class WorkSchedule(models.Model):   # Рабочий график времени на день
    datetime_start = models.TimeField(verbose_name='Начало времени')
    datetime_end = models.TimeField(verbose_name='Конец времени')

    def __str__(self):
        return f'{self.datetime_start} - {self.datetime_end}'

    class Meta:
        verbose_name = 'Рабочий график'
        verbose_name_plural = 'Рабочие графики'


class Days(models.Model):   # Дни
    date = models.CharField(max_length=150, verbose_name='Дата')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class WorkDaysSchedule(models.Model):   # График работы врача
    day = models.ForeignKey(Days,
                            on_delete=models.CASCADE,
                            related_name='wds',
                            verbose_name='День')
    doctor = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Доктор')
    schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, verbose_name='График')

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name = 'Расписание рабочих дней'
        verbose_name_plural = 'Расписание рабочих дней'