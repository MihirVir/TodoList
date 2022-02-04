# Generated by Django 3.2.7 on 2022-01-26 14:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('taskId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('taskName', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
