# Generated by Django 4.0.5 on 2022-08-23 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0003_alter_todolist_created_alter_todolist_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='task_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist', to=settings.AUTH_USER_MODEL),
        ),
    ]