# Generated by Django 3.0.5 on 2020-05-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200504_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_subtask',
        ),
    ]