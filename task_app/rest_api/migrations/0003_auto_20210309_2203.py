# Generated by Django 3.1.7 on 2021-03-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20210309_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False, help_text='Status Task, True-Complete/False-Incomplete', verbose_name='status'),
        ),
    ]
