# Generated by Django 4.2.1 on 2023-07-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_section_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.FileField(upload_to='markdown/resume/'),
        ),
    ]
