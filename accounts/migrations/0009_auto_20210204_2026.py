# Generated by Django 2.1.5 on 2021-02-05 01:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210204_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('81c11744-872b-42fb-ba0a-6ccaeedba034'), editable=False, primary_key=True, serialize=False),
        ),
    ]