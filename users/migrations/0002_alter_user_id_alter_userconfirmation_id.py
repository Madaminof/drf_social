# Generated by Django 5.0.6 on 2024-06-25 19:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('19971c96-f517-49cb-bd67-50ffe91aaa8f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('19971c96-f517-49cb-bd67-50ffe91aaa8f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
