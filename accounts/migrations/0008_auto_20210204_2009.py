# Generated by Django 2.1.5 on 2021-02-05 01:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210204_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d5465775-4a2b-4c05-afa9-57232c90301c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
