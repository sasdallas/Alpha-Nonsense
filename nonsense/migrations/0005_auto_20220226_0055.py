# Generated by Django 3.1.5 on 2022-02-26 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nonsense', '0004_user_feedoption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='html',
        ),
    ]