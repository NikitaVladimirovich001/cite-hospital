# Generated by Django 4.2 on 2024-03-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=0, verbose_name='Модератор'),
        ),
    ]
