# Generated by Django 2.1.5 on 2021-02-06 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210206_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('949babf5-b8b6-4b55-8e4f-a141fe05c6b5'), editable=False, primary_key=True, serialize=False),
        ),
    ]
