# Generated by Django 4.2.1 on 2023-07-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_project_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
