# Generated by Django 2.1.5 on 2021-02-02 23:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210202_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0a795306-0e9e-40bf-95cf-60b1c2aac145'), editable=False, primary_key=True, serialize=False),
        ),
    ]
