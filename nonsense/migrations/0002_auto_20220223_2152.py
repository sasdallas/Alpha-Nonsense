# Generated by Django 3.1.5 on 2022-02-23 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nonsense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
