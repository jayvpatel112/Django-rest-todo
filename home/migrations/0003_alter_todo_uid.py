# Generated by Django 4.2.6 on 2023-11-02 12:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_created_at_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('fb3c6b7c-c97b-448e-8898-2261e933f7bc'), editable=False, primary_key=True, serialize=False),
        ),
    ]
