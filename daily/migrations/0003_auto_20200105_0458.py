# Generated by Django 2.2.7 on 2020-01-05 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0002_auto_20200104_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='context1',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='context2',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='context3',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='header1',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='header2',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='header3',
        ),
    ]
