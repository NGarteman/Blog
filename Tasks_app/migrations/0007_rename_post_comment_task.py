# Generated by Django 3.2.9 on 2021-11-20 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks_app', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='task',
        ),
    ]
