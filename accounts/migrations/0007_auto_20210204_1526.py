# Generated by Django 2.1.5 on 2021-02-04 20:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210202_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('049862e4-f118-4f65-bf92-ec6355fb540d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
