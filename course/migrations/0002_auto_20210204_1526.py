# Generated by Django 2.1.5 on 2021-02-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Requirements',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_what_you_will_learn',
            field=models.TextField(null=True),
        ),
    ]