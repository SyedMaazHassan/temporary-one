# Generated by Django 2.1.5 on 2021-02-01 23:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210131_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('daad8c79-581d-46dc-91a2-62c00bae0a49'), editable=False, primary_key=True, serialize=False),
        ),
    ]
