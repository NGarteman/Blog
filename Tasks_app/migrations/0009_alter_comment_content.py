# Generated by Django 3.2.9 on 2021-11-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks_app', '0008_auto_20211120_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
