# Generated by Django 3.1.5 on 2022-02-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonsense', '0005_auto_20220226_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
    ]
