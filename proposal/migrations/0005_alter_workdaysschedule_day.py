# Generated by Django 4.2 on 2024-03-11 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0004_alter_workschedule_datetime_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdaysschedule',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wds', to='proposal.days', verbose_name='День'),
        ),
    ]
